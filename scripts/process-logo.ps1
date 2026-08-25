Add-Type -AssemblyName System.Drawing

$assets = "C:\Users\Lyneth Lendez\Websites\W-Divers-Coron\assets"
$srcPath = "$assets\logo-source.png"

function Save-Png {
    param($bitmap, $outPath)
    $bitmap.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Png)
}

function Make-Transparent {
    param($bitmap, $threshold = 235)
    # Returns a new 32bpp ARGB bitmap where near-white pixels become transparent.
    $w = $bitmap.Width
    $h = $bitmap.Height
    $out = New-Object System.Drawing.Bitmap($w, $h, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
    $srcData = $bitmap.LockBits((New-Object System.Drawing.Rectangle(0,0,$w,$h)), [System.Drawing.Imaging.ImageLockMode]::ReadOnly, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
    $dstData = $out.LockBits((New-Object System.Drawing.Rectangle(0,0,$w,$h)), [System.Drawing.Imaging.ImageLockMode]::WriteOnly, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
    $bytes = $w * $h * 4
    $buffer = New-Object byte[] $bytes
    [System.Runtime.InteropServices.Marshal]::Copy($srcData.Scan0, $buffer, 0, $bytes)
    for ($i = 0; $i -lt $bytes; $i += 4) {
        $b = $buffer[$i]
        $g = $buffer[$i+1]
        $r = $buffer[$i+2]
        if ($r -ge $threshold -and $g -ge $threshold -and $b -ge $threshold) {
            $buffer[$i+3] = 0
        }
    }
    [System.Runtime.InteropServices.Marshal]::Copy($buffer, 0, $dstData.Scan0, $bytes)
    $bitmap.UnlockBits($srcData)
    $out.UnlockBits($dstData)
    return $out
}

function Get-OpaqueBBox {
    param($bitmap)
    $w = $bitmap.Width
    $h = $bitmap.Height
    $minX = $w; $minY = $h; $maxX = 0; $maxY = 0
    $data = $bitmap.LockBits((New-Object System.Drawing.Rectangle(0,0,$w,$h)), [System.Drawing.Imaging.ImageLockMode]::ReadOnly, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
    $bytes = $w * $h * 4
    $buffer = New-Object byte[] $bytes
    [System.Runtime.InteropServices.Marshal]::Copy($data.Scan0, $buffer, 0, $bytes)
    for ($y = 0; $y -lt $h; $y++) {
        $rowBase = $y * $w * 4
        for ($x = 0; $x -lt $w; $x++) {
            $idx = $rowBase + $x * 4
            $alpha = $buffer[$idx+3]
            if ($alpha -gt 10) {
                if ($x -lt $minX) { $minX = $x }
                if ($x -gt $maxX) { $maxX = $x }
                if ($y -lt $minY) { $minY = $y }
                if ($y -gt $maxY) { $maxY = $y }
            }
        }
    }
    $bitmap.UnlockBits($data)
    return @{ X = $minX; Y = $minY; W = ($maxX - $minX + 1); H = ($maxY - $minY + 1) }
}

function Crop {
    param($bitmap, $x, $y, $w, $h)
    $rect = New-Object System.Drawing.Rectangle($x, $y, $w, $h)
    $out = New-Object System.Drawing.Bitmap($w, $h, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
    $g = [System.Drawing.Graphics]::FromImage($out)
    $g.DrawImage($bitmap, (New-Object System.Drawing.Rectangle(0,0,$w,$h)), $rect, [System.Drawing.GraphicsUnit]::Pixel)
    $g.Dispose()
    return $out
}

function Resize {
    param($bitmap, $maxDim)
    $w = $bitmap.Width; $h = $bitmap.Height
    if ($w -ge $h) { $newW = $maxDim; $newH = [int]([double]$h * $maxDim / $w) }
    else { $newH = $maxDim; $newW = [int]([double]$w * $maxDim / $h) }
    $out = New-Object System.Drawing.Bitmap($newW, $newH, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
    $g = [System.Drawing.Graphics]::FromImage($out)
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
    $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
    $g.DrawImage($bitmap, 0, 0, $newW, $newH)
    $g.Dispose()
    return $out
}

# Load source
$src = [System.Drawing.Bitmap]::FromFile($srcPath)
Write-Output "Source: $($src.Width) x $($src.Height)"

# Step 1: isolate icon-only region (exclude wordmark below). Source is 1254x1254.
# Icon mark sits roughly in the upper-middle band; wordmark text starts further down.
$iconRegion = Crop -bitmap $src -x 200 -y 240 -w 850 -h 520
$iconTransparent = Make-Transparent -bitmap $iconRegion -threshold 235
$bbox = Get-OpaqueBBox -bitmap $iconTransparent
Write-Output "Icon bbox: X=$($bbox.X) Y=$($bbox.Y) W=$($bbox.W) H=$($bbox.H)"

# pad bbox by a small margin
$pad = 14
$px = [Math]::Max(0, $bbox.X - $pad)
$py = [Math]::Max(0, $bbox.Y - $pad)
$pw = [Math]::Min($iconTransparent.Width - $px, $bbox.W + $pad * 2)
$ph = [Math]::Min($iconTransparent.Height - $py, $bbox.H + $pad * 2)
$iconTight = Crop -bitmap $iconTransparent -x $px -y $py -w $pw -h $ph
$iconResized = Resize -bitmap $iconTight -maxDim 480
Save-Png -bitmap $iconResized -outPath "$assets\logo-mark.png"
Write-Output "Saved logo-mark.png ($($iconResized.Width) x $($iconResized.Height))"

# Step 2: full logo (icon + wordmark), background transparent, tightly cropped
$fullTransparent = Make-Transparent -bitmap $src -threshold 235
$fullBbox = Get-OpaqueBBox -bitmap $fullTransparent
$fpad = 20
$fx = [Math]::Max(0, $fullBbox.X - $fpad)
$fy = [Math]::Max(0, $fullBbox.Y - $fpad)
$fw = [Math]::Min($fullTransparent.Width - $fx, $fullBbox.W + $fpad * 2)
$fh = [Math]::Min($fullTransparent.Height - $fy, $fullBbox.H + $fpad * 2)
$fullTight = Crop -bitmap $fullTransparent -x $fx -y $fy -w $fw -h $fh
$fullResized = Resize -bitmap $fullTight -maxDim 900
Save-Png -bitmap $fullResized -outPath "$assets\logo-full.png"
Write-Output "Saved logo-full.png ($($fullResized.Width) x $($fullResized.Height))"

# Step 3: favicon — composite the icon mark onto a small rounded navy square for tab-bar legibility
$favSize = 128
$favCanvas = New-Object System.Drawing.Bitmap($favSize, $favSize, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
$g = [System.Drawing.Graphics]::FromImage($favCanvas)
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$navyBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(255, 10, 42, 64))
$path = New-Object System.Drawing.Drawing2D.GraphicsPath
$r = 26
$rectF = New-Object System.Drawing.Rectangle(0, 0, $favSize, $favSize)
$path.AddArc(0, 0, $r*2, $r*2, 180, 90)
$path.AddArc($favSize-$r*2, 0, $r*2, $r*2, 270, 90)
$path.AddArc($favSize-$r*2, $favSize-$r*2, $r*2, $r*2, 0, 90)
$path.AddArc(0, $favSize-$r*2, $r*2, $r*2, 90, 90)
$path.CloseFigure()
$g.FillPath($navyBrush, $path)
# scale icon mark to fit within padded area
$iconForFav = Resize -bitmap $iconTight -maxDim ([int]($favSize * 0.72))
$ix = [int](($favSize - $iconForFav.Width) / 2)
$iy = [int](($favSize - $iconForFav.Height) / 2)
$g.DrawImage($iconForFav, $ix, $iy, $iconForFav.Width, $iconForFav.Height)
$g.Dispose()
Save-Png -bitmap $favCanvas -outPath "$assets\favicon.png"
Write-Output "Saved favicon.png"

Write-Output "Done."

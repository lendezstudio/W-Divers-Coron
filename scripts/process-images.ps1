Add-Type -AssemblyName System.Drawing

$src = "C:\Users\Lyneth Lendez\Downloads"
$dest = "C:\Users\Lyneth Lendez\Websites\W-Divers-Coron\assets\images"
if (-not (Test-Path $dest)) { New-Item -ItemType Directory -Force -Path $dest | Out-Null }

function Save-Jpeg {
    param($bitmap, $outPath, $quality = 85)
    $codec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
    $params = New-Object System.Drawing.Imaging.EncoderParameters(1)
    $params.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [int64]$quality)
    $bitmap.Save($outPath, $codec, $params)
}

function Resize-Image {
    param($bitmap, $maxDim)
    $w = $bitmap.Width
    $h = $bitmap.Height
    if ($w -le $maxDim -and $h -le $maxDim) { return $bitmap }
    if ($w -ge $h) {
        $newW = $maxDim
        $newH = [int]([double]$h * $maxDim / $w)
    } else {
        $newH = $maxDim
        $newW = [int]([double]$w * $maxDim / $h)
    }
    $resized = New-Object System.Drawing.Bitmap($newW, $newH)
    $g = [System.Drawing.Graphics]::FromImage($resized)
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
    $g.DrawImage($bitmap, 0, 0, $newW, $newH)
    $g.Dispose()
    $bitmap.Dispose()
    return $resized
}

function Process-Simple {
    param($srcFile, $outName, $maxDim, $quality = 85)
    $img = [System.Drawing.Bitmap]::FromFile("$src\$srcFile")
    $resized = Resize-Image -bitmap $img -maxDim $maxDim
    Save-Jpeg -bitmap $resized -outPath "$dest\$outName" -quality $quality
    $resized.Dispose()
    Write-Output "Saved $outName"
}

function Process-CropBottom {
    param($srcFile, $outName, $cropPx, $maxDim, $quality = 85)
    $img = [System.Drawing.Bitmap]::FromFile("$src\$srcFile")
    $newHeight = $img.Height - $cropPx
    $cropped = New-Object System.Drawing.Bitmap($img.Width, $newHeight)
    $g = [System.Drawing.Graphics]::FromImage($cropped)
    $srcRect = New-Object System.Drawing.Rectangle(0, 0, $img.Width, $newHeight)
    $g.DrawImage($img, $srcRect, $srcRect, [System.Drawing.GraphicsUnit]::Pixel)
    $g.Dispose()
    $img.Dispose()
    $resized = Resize-Image -bitmap $cropped -maxDim $maxDim
    Save-Jpeg -bitmap $resized -outPath "$dest\$outName" -quality $quality
    $resized.Dispose()
    Write-Output "Saved $outName (cropped)"
}

# Hero — diver entering wreck opening (split shot)
Process-Simple "482008797_1107942958010614_5747178299618558990_n.jpg" "hero-wreck-entry.jpg" 1400

# Home feature: group at the shop, wreck-site map wall
Process-Simple "480783055_1096620732476170_8834330674928734210_n.jpg" "group-shop-lounge.jpg" 1400

# Home feature: team + guests at shop, "W Divers Coron" wall sign — crop out Huawei watermark strip at bottom
Process-CropBottom "481216300_1096660412472202_7706288797344496579_n.jpg" "team-shop-interior.jpg" 95 1400

# Dive-trips: wreck diving split shot (interior wreck, diver with light)
Process-Simple "482208487_1107942858010624_1853207215717012350_n.jpg" "wreck-diving-splitshot.jpg" 1400

# Dive-trips: reef diving, coral bommie + diver
Process-Simple "487136721_1125033836301526_4788566768362006990_n.jpg" "reef-diving-coral.jpg" 1400

# Dive-trips: island hopping, boat + turquoise water + islands
Process-Simple "487165067_1126635972807979_1844607446905230639_n.jpg" "island-hopping-boat.jpg" 1400

# Gallery images
Process-Simple "485848655_1119004903571086_4783159311121457415_n.jpg" "gallery-wreck-reef-fish.jpg" 1000
Process-Simple "482222691_1112454450892798_7892061487699634058_n.jpg" "gallery-two-divers.jpg" 1000
Process-Simple "484589839_1115778423893734_7980219096247502692_n.jpg" "gallery-turtle.jpg" 1000
Process-Simple "482979728_1109530821185161_1940194183424630241_n.jpg" "gallery-boat-hull.jpg" 1000
Process-Simple "485003963_1115471980591045_921063625741462737_n.jpg" "gallery-storefront.jpg" 1000
Process-Simple "488646099_1133394878798755_3407493243801420763_n.jpg" "gallery-food.jpg" 1000
Process-Simple "487994222_1128062919331951_4203145138619336251_n.jpg" "gallery-sunset-group.jpg" 1000

Write-Output "Done."

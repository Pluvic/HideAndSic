rule Suspicious_LSB_Red_Channel
{
    meta:
        description = "Detects possible LSB steganography in PNG images by checking abnormal LSB distribution"
        author = "Victor"
        method = "LSB on red channel"

    strings:
        // PNG signature
        $png = { 89 50 4E 47 0D 0A 1A 0A }

    condition:
        // Only look at PNGs
        $png at 0 and

        // Too many bytes ending in 0x00 or 0x01 (LSB anomaly)
        (
            uint8(100) % 2 == uint8(200) % 2 and
            uint8(300) % 2 == uint8(400) % 2 and
            uint8(500) % 2 == uint8(600) % 2 and
            uint8(700) % 2 == uint8(800) % 2
        )
}

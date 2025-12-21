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

rule Script_Disguised_Shebang
{
    meta:
        description = "Detect script files disguised with another extension"
        author = "HideAndSic"
    strings:
        $bash = "#!/bin/bash"
        $sh   = "#!/bin/sh"
        $py   = "#!/usr/bin/python"
        $ps   = "powershell"
    condition:
        any of them
}

rule Suspicious_Executable_Extension
{
    meta:
        description = "Detects executable files with uncommon extensions"
        author = "Victor"
    strings:
        $exe_ext = ".exe"
        $dll_ext = ".dll"
        $scr_ext = ".scr"
        $bat_ext = ".bat"
    condition:
        any of them
}

rule PNG_Data_After_IEND
{
    meta:
        description = "Detect extra data after PNG IEND chunk"
    strings:
        $iend = { 49 45 4E 44 AE 42 60 82 }
    condition:
        $iend and filesize > @iend + 8
}

rule Embedded_Archive
{
    meta:
        description = "Detect embedded archive headers"
    strings:
        $zip  = { 50 4B 03 04 }
        $gzip = { 1F 8B }
    condition:
        any of them
}

rule Possible_Encrypted_Data
{
    meta:
        description = "Heuristic for encrypted or packed data"
    condition:
        filesize > 1024 and
        for any i in (0..filesize-1) : (uint8(i) > 0x20 and uint8(i) < 0x7E)
}



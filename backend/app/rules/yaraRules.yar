rule Suspicious_File {
    meta:
        description = "Detects files with suspicious characteristics"
        author = "Security Team"
        date = "2025-11-20"
        version = "1.0"

    strings:
        $mz = "MZ"
        $pe = "PE"
        $upx = "UPX"
        
    condition:
        $mz at 0 or $pe or $upx
}
# This file will contain the logic for analyzing files

import magic
import yara
from app.utils import calculateHashes, calculateEntropy

YARA_RULES_PATH = "app/rules/yaraRules.yar"

def analyzeFile(filePath: str) -> dict:
    # Calculate file hashes
    hashes = calculateHashes(filePath)

    # Determine MIME type
    mime = magic.Magic(mime=True)
    mimeType = mime.from_file(filePath)

    # Calculate entropy
    entropy = calculateEntropy(filePath)

    # YARA scanning
    yaraRules = yara.compile(filepath=YARA_RULES_PATH)
    yaraMatches = yaraRules.match(filePath)
    yaraResults = [str(match) for match in yaraMatches]
    yaraDetected = len(yaraResults) > 0

    return {
        "hashes": hashes,
        "mime_type": mimeType,
        "entropy": entropy,
        "yara_detected": yaraDetected,
        "yara_results": yaraResults,
    }
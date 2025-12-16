<script>
    import { scanFile } from "../lib/api.js";

    let file = null;
    let isDragging = false;
    let result = null

    // Handle file drop event
    function handleDrop(e) {
        e.preventDefault();
        isDragging = false;

        if (e.dataTransfer.files.length > 0) {
            file = e.dataTransfer.files[0];
        }
    }

    // Handle drag over event
    function handleDragOver(e) {
        e.preventDefault();
        isDragging = true;
    }

    // Handle drag leave event
    function handleDragLeave(e) {
        e.preventDefault();
        isDragging = false;
    }

    // Handle file upload and analyze data
    async function handleUpload(file) {
        if (!file) return;
        result = await scanFile(file);
        file = null;
        console.log(result);
    }

</script>

<div class="container">
    <div
        class="dragAndDrop"
        class:border-blue-500={isDragging}
        class:border-gray-300={!isDragging}
        role="button"
        tabindex="0"
        aria-label="Sélectionner un fichier ou glisser-déposer ici"
        on:keydown={() => handleUpload(file)}
        on:drop={handleDrop}
        on:dragover={handleDragOver}
        on:dragleave={handleDragLeave}
        on:click={() => document.getElementById('fileInput').click()}
    >
        <input style="display: none;" type="file" id="fileInput" on:change={(e) => { file = e.target.files[0]; }} aria-label="File input for analysis" />
        {#if file}
            <p class="text-gray-700 text-lg">
                File loaded: <strong>{file.name}</strong>
            </p>
        {:else}
            <p class="text-gray-500 text-xl">
                Drag and drop a file here or click to select
            </p>
        {/if}
  </div>


    {#if file}
    <button on:click={() => handleUpload(file)} class="AnalyzeButton">
        Analyze
    </button>
    {/if}

    {#if result}
    <div class="PopUpResult" on:click={() => { result = false; }} on:keydown={() => { result = false; }} role="button" tabindex="0" aria-label="Close analysis result">
        <h2>Analysis Result</h2>

        <div class="section">
            <strong>File</strong>
            <p>{file.name}</p>
        </div>

        <div class="section">
            <strong>Hashes</strong>
            <ul class="hashes">
                <li><span>MD5</span>{result.hashes.md5}</li>
                <li><span>SHA1</span>{result.hashes.sha1}</li>
                <li><span>SHA256</span>{result.hashes.sha256}</li>
            </ul>
        </div>

        <div class="section">
            <strong>MIME Type</strong>
            <p>{result.mime_type}</p>
        </div>

        <div class="section">
            <strong>Entropy</strong>

            <div class="entropy-bar">
                <div
                    class="entropy-fill"
                    style="
                        width: {(result.entropy / 8) * 100}%;
                        background-color: hsl({120 - (result.entropy / 8) * 120}, 70%, 50%);
                    "
                ></div>
                <span class="entropy-value">
                    {result.entropy.toFixed(2)} / 8
                </span>
            </div>
        </div>

        <div class="section">
            <strong>YARA Detection</strong>
            <p class={result.yara_detected ? 'danger' : 'safe'}>
                {result.yara_detected ? 'Detected' : 'None'}
            </p>

            {#if result.yara_detected}
                <ul class="yara-list">
                    {#each result.yara_results as yara}
                        <li>{yara}</li>
                    {/each}
                </ul>
            {/if}
        </div>
    </div>
{/if}

</div>

<style>
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background-color: rgb(255, 255, 255);
        position: relative;
    }

    .dragAndDrop {
        border: 4px dashed;
        border-radius: 8px;
        background-color: rgb(239, 239, 239);
        text-align: center;
        vertical-align: middle;
        cursor: pointer;
        transition: border-color 0.3s;
        height: calc(100vh - 15em);
        width: calc(100vw - 6em);
        margin: 3em 3em;
    }

    .AnalyzeButton {
        background-color: hwb(120 9% 30%);
        padding: 0.75rem 1.5rem;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 1rem;
        transition: background-color 0.3s;
        position: absolute;
        bottom: 10em;
    }

    .AnalyzeButton:hover {
        background-color: #357ABD;
    }

    .PopUpResult {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);

    background-color: #ffffff;
    border-radius: 10px;
    padding: 1.5em;

    width: 80%;
    max-width: 700px;
    max-height: 80vh;
    overflow-y: auto;

    z-index: 1000;

    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }


    .PopUpResult h2 {
    margin-top: 0;
    text-align: center;
    }

    .section {
        margin-bottom: 1em;
    }

    .section strong {
        display: block;
        margin-bottom: 0.3em;
    }

    .hashes {
        list-style: none;
        padding: 0;
        font-family: monospace;
        font-size: 0.85rem;
    }

    .hashes li {
        display: flex;
        gap: 0.5em;
    }

    .hashes span {
        width: 70px;
        font-weight: bold;
    }

    .entropy-bar {
        position: relative;
        height: 24px;
        background-color: #ddd;
        border-radius: 12px;
        overflow: hidden;
    }

    .entropy-fill {
        height: 100%;
        transition: width 0.4s ease;
    }

    .entropy-value {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-weight: bold;
        color: #000;
    }

    .safe {
        color: green;
        font-weight: bold;
    }

    .danger {
        color: red;
        font-weight: bold;
    }

    .yara-list {
        margin-top: 0.5em;
        padding-left: 1.2em;
    }

</style>
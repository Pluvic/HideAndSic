<script>
    import { extractData } from "../lib/api.js";

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

    // Handle file upload and extract data
    async function handleUpload(file) {
        if (!file) return;
        result = await extractData(file);
    }

</script>

<div class="container">
    <div
        class="dragAndDrop"
        class:border-blue-500={isDragging}
        class:border-gray-300={!isDragging}
        role="button"
        tabindex="0"
        aria-label="Select an image file or drag and drop here"
        on:keydown={() => handleUpload(file)}
        on:drop={handleDrop}
        on:dragover={handleDragOver}
        on:dragleave={handleDragLeave}
        on:click={() => document.getElementById('fileInput').click()}
    >
        <input style="display: none;" type="file" id="fileInput" on:change={(e) => { file = e.target.files[0]; }} />
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
    <button on:click={() => handleUpload(file)} class="ExtractButton">
        Extract
    </button>
    {/if}

    {#if result}
        <div class = "PopUpResult">
            <h2>Result :</h2>
            <h3>Extracted Data:</h3>
            <p>{result.message}</p>
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

    .ExtractButton {
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

    .ExtractButton:hover {
        background-color: #357ABD;
    }

    .PopUpResult {
        position: absolute;
        top: 10em;
        left: 50%;
        transform: translateX(-50%);
        background-color: rgb(255, 255, 255);
        border: 2px solid rgb(0, 0, 0);
        border-radius: 8px;
        padding: 1em;
        max-width: 80%;
        max-height: 60vh;
        overflow-y: auto;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
</style>
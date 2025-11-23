<script>
    import { hideData } from "../lib/api.js";

    let file = null;
    let message = "";
    let isDragging = false;
    let url = null;
    let filename = null;

    function handleDrop(e) {
        e.preventDefault();
        isDragging = false;

        if (e.dataTransfer.files.length > 0) {
            file = e.dataTransfer.files[0];
        }
    }

    function handleDragOver(e) {
        e.preventDefault();
        isDragging = true;
    }

    function handleDragLeave(e) {
        e.preventDefault();
        isDragging = false;
    }
    
    let result = null

    async function handleUpload(image) {
        if (!image || message === "") return;
        result = await hideData(image, message);

        // Create a URL for the returned image blob
        url = URL.createObjectURL(result.blob);
        filename = result.filename;

        // --- FORCED DOWNLOAD ---
        const link = document.createElement("a");
        link.href = url;
        link.download = filename;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);

        // optional : cleanup
        URL.revokeObjectURL(url);
}


</script>

<!-- Grande zone drag & drop -->
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
          Drag and drop an image here or click to select
        </p>
      {/if}
  </div>
  <div class= "messageInput">
    <input type="text" placeholder="Enter message to hide" bind:value={message} />
  </div>


  {#if file && message !== ""}
  <button on:click={() => handleUpload(file)} class="AnalyzeButton">
      Hide
  </button>
  {/if}

</div>

<style>
    .container {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        position: relative;
        background-color: white;
    }

    .messageInput {
        border: 4px solid;
        border-radius: 8px;
        background-color: rgb(239, 239, 239);
        height: calc(100vh - 15em);
        margin: 1em;
        display: flex;
        justify-content: center;
        width: 100%;
    }

    input[type="text"] {
        vertical-align: middle;
        height: 5%;
        width: 80%;
        margin-top:30%;
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
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        padding: 0.75rem 1.5rem;
        border-radius: 10px;
        cursor: pointer;
        font-size: 1rem;
        transition: background-color 0.3s;
        position: absolute;
        bottom: 2em;
        width: 10em;
        height: 3em;
    }

    .AnalyzeButton:hover {
        background-color: #357ABD;
    }

</style>
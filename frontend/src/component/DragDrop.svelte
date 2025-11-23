<script>
    export let onAnalyze = (file) => {};

    let file = null;
    let isDragging = false;

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

    function handleAnalyze() {
        if (file) {
            onAnalyze(file);
        }
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
        aria-label="Sélectionner un fichier ou glisser-déposer ici"
        on:keydown={handleAnalyze}
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
  <button on:click={handleAnalyze} class="AnalyzeButton">
      Analyze
  </button>
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
</style>
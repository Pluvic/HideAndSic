<script>
    import DragDrop from "./component/DragDrop.svelte";
    import { scanFile } from "./lib/api.js";
    
    let result = null

    async function handleUpload(file) {
        if (!file) return;
        result = await scanFile(file);
    }
</script>

<main>
    <header>
        <h1>Hide&Sic</h1>
    </header>
    <DragDrop onAnalyze={handleUpload} />

	{#if result}
    <div class = "PopUpResult">
		<h2>Result :</h2>
		<pre>{JSON.stringify(result, null, 2)}</pre>
    </div>
	{/if}
</main>

<style>
    main {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        position: relative;
    }


    header {
        background-color: rgb(54, 54, 54);
        height: 8em;
        box-shadow: 0 2px 8px rgb(255, 255, 255);
    }
    h1 {
        color:white;
        padding: 0.5em;
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
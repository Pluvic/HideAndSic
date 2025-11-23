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
		<h2>Result :</h2>
		<pre>{JSON.stringify(result, null, 2)}</pre>
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
</style>
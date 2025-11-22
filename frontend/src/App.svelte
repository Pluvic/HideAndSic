<script>
    import { scanFile } from "./lib/api.js";
    
    let file;
    let result = null

    async function handleUpload() {
        if (!file) return;
        result = await scanFile(file);
    }
</script>

<main>
    <h1>HideAndSic</h1>
    <input type="file" on:change={(e) => (file = e.target.files[0])} />

	<button on:click={handleUpload}>Analyze</button>

	{#if result}
		<h2>Result :</h2>
		<pre>{JSON.stringify(result, null, 2)}</pre>
	{/if}
</main>
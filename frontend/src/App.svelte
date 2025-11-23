<script>
    import Analyze from "./component/Analyze.svelte";
    import Hide from "./component/Hide.svelte";
    import Extract from "./component/Extract.svelte";
    import { currentPage } from "./store/store.js";
</script>

<main>
    <header>
        <h1>Hide&Sic</h1>

        <nav>
            <button on:click={() => currentPage.set('analyze')}>Analyze</button>
            <button on:click={() => currentPage.set('hide')}>Hide</button>
            <button on:click={() => currentPage.set('extract')}>Extract</button>
        </nav>
    </header>

    {#if $currentPage === 'analyze'}
        <Analyze />
    {:else if $currentPage === 'hide'}
        <Hide />
    {:else if $currentPage === 'extract'}
        <Extract />
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
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: rgb(54, 54, 54);
        height: 8em;
        box-shadow: 0 2px 8px rgb(255, 255, 255);
    }
    h1 {
        color:white;
        padding: 0.5em;
    }

    nav button {
        margin: 0 1em;
        padding: 0.5em 1em;
        font-size: 1em;
        border: none;
        border-radius: 4px;
        background-color: rgb(100, 100, 100);
        color: white;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    
</style>
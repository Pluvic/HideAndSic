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
            {#if $currentPage === 'analyze'}
                <button on:click={() => currentPage.set('analyze')} style='background-color: rgb(100, 100, 100);'>Analyze</button>
            {:else}
                <button on:click={() => currentPage.set('analyze')} style='background-color: transparent;'>Analyze</button>
            {/if}

            {#if $currentPage === 'hide'}
                <button on:click={() => currentPage.set('hide')} style='background-color: rgb(100, 100, 100);'>Hide</button>
            {:else}
                <button on:click={() => currentPage.set('hide')} style='background-color: transparent;'>Hide</button>
            {/if}

            {#if $currentPage === 'extract'}
                <button on:click={() => currentPage.set('extract')} style='background-color: rgb(100, 100, 100);'>Extract</button>
            {:else}
                <button on:click={() => currentPage.set('extract')} style='background-color: transparent;'>Extract</button>
            {/if}
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
    /* Style for the main container */
    main {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        position: relative;
    }

    /* Style for the header */
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
        font-size: 1em;
        border: none;
        border-radius: 4px;
        color: white;
        cursor: pointer;
        transition: background-color 0.3s;
        height: 8em;
        width: 8em;
    }
    
</style>
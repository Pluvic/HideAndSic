// This file contains functions to interact with the backend API for scanning files, hiding data, and extracting data

// This function sends a file to the backend for scanning
export async function scanFile(file) {
    const form = new FormData();
    form.append('file', file);

    const res = await fetch("http://localhost:8000/scan", {
        method: "POST",
        body: form
    });

    if (!res.ok) {
        throw new Error(`Error scanning file: ${res.statusText}`);
    }

    return await res.json();
}

// This function sends an image and a message to the backend to hide the message within the image
export async function hideData(image, message, encrypt=false) {
    const form = new FormData();
    form.append('image', image);
    form.append('message', message);
    form.append('encrypt', encrypt);

    const res = await fetch("http://localhost:8000/hide", {
        method: "POST",
        body: form
    });

    if (!res.ok) {
        throw new Error(`Error hiding data: ${res.statusText}`);
    }

    const blob = await res.blob();
    return {
        filename: "encoded_" + image.name,
        blob: blob
    };
}

// This function sends an image to the backend to extract hidden data from it
export async function extractData(image) {
    const form = new FormData();
    form.append('image', image);
    
    const res = await fetch("http://localhost:8000/extract", {
        method: "POST",
        body: form
    });

    if (!res.ok) {
        throw new Error(`Error extracting data: ${res.statusText}`);
    }

    return await res.json();
}

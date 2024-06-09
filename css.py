def get_css():
    css = """
/* Your CSS code for professional documentation goes here */
body {
    font-family: Arial, sans-serif;
    line-height: 1.5;
    padding: 0;
    background-color: #333;
    color: #ddd;
}

h1 {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
}

h2 {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 16px;
}

p {
    margin-bottom: 12px;
}

code {
    font-family: Consolas, monospace;
    background-color: #232323;
    padding: 2px 4px;
    border-radius: 4px;
    color: #ddd;
}

pre > code {
    display: block;
    padding: 16px;
    margin: 0;
    overflow: auto;
    font-size: 85%;
    line-height: 1.45;
    border-radius: 6px;
}

.highlight {
    background-color: #232323 !important;
    padding: 16px !important;
    margin: 16px 0 !important;
    overflow: auto !important;
    border-radius: 6px !important;
}

.sidebar {
    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
    width: 200px;
    background-color: #222;
    padding: 5px;
    overflow: auto;
    border-bottom-right-radius: 10px;
    border-top-right-radius: 10px;
}

.sidebar h1 {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 16px;
    text-align: center;
}

/* Styles for the main content */
.main-content {
    margin-left: 220px;
    padding: 5px;
}

a {
    color: #ddd;
    padding: 2px;
}

a:hover {
    border-radius: 4px;
    background-color: #111222;
}

/* Style the scrollbar */
.sidebar::-webkit-scrollbar {
    width: 10px;
}

.sidebar::-webkit-scrollbar-track {
    background: #333;
}

.sidebar::-webkit-scrollbar-thumb {
    background: #555;
}

/* Add more styles as needed */
"""
    return css

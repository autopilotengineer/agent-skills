# Compatibility plan

Document before editing:

1. Supported Node, browser, bundler, and downstream consumer versions.
2. Package type, entry points, conditional exports, declaration paths, and deep imports.
3. Current compiler version, inherited configs, module/moduleResolution pair, interop flags, strictness, emit, and source maps.
4. Runtime execution path: compiled JavaScript, loader, transpile-on-run, bundler, or framework compiler.
5. Test and lint integration with TypeScript.
6. Ordered changes, proof for each step, and rollback boundary.

Test packages as consumers would: packed artifact, public imports, both module systems when promised, declarations, and supported runtimes. Treat a framework's TypeScript constraints as part of the compatibility contract.

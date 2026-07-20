# Server evaluation

Evaluate a candidate in this order:

1. Confirm the repository has a recurring capability gap.
2. Search the official MCP Registry and follow its source link.
3. Verify publisher identity, recent maintenance, license, released versions, and issue/security posture.
4. Enumerate tools and label each read, write, destructive, or administrative.
5. Determine transport, network listeners, authentication, telemetry, filesystem scope, and secret storage.
6. Design the minimum enabled tool subset, read-only/development credentials, scoped roots, and approval gates.
7. Compare it with built-in host tools and the no-server option.

Reject candidates whose source or permissions cannot be inspected, whose access materially exceeds the need, or whose capability duplicates safer tools already available.

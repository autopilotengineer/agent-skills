# Next.js audit evidence

Use the lockfile-resolved version and official Next.js documentation. Audit the router actually present.

## App Router

- route groups, layouts, templates, parallel/intercepting routes, handlers, and middleware/proxy
- Server/Client boundaries and serializable props
- data fetching, request memoization, cache APIs, revalidation, dynamic rendering, and mutations
- loading, error, not-found, metadata, images, fonts, and accessibility

## Pages Router

- page/API route boundaries, custom app/document/error pages
- `getStaticProps`, `getStaticPaths`, `getServerSideProps`, client fetching, and ISR behavior
- middleware, metadata/head, images, and deployment output

## Both

Check authentication versus authorization at every server entry point, environment-variable exposure, CSRF/origin assumptions for mutations, redirects, headers/cookies, runtime compatibility, bundle impact, hydration, testing, logging, and hosting constraints. In hybrid projects, examine navigation and shared-module boundaries between routers.

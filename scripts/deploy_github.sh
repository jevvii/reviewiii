#!/bin/bash
set -e

echo "🔨 Building Astro production site..."
bun run build

echo "📦 Syncing dist to docs/..."
rm -rf docs/_astro
cp -r dist/* docs/
touch docs/.nojekyll

echo "🚀 Pushing main branch to origin..."
git push origin main

echo ""
echo "✅ Successfully deployed to GitHub!"
echo "Your GitHub Pages site is live at:"
echo "👉 https://jevvii.github.io/reviewiii/"

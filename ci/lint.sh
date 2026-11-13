#!/bin/sh
# The `lint` check: the blog's Markdown (content/ in both languages, archetypes/, README.md) with markdownlint-cli2,
# pinned below, and the settings in .markdownlint-cli2.jsonc: markdownlint's default rules, less line length and
# descriptive link text, which are about the prose. The theme is not here (the Dockerfile fetches it), so nothing
# Hugo renders is checked: the `build` check does that.
#
# yggdrasil.yml runs it in the pinned Node image (Alpine: POSIX sh) from the repository's root. By hand:
#   docker run --rm -v "$PWD:/src" -w /src <image from yggdrasil.yml> sh ci/lint.sh
set -eu

# The repository's root, wherever this is run from.
cd "$(dirname "$0")/.."

# renovate: datasource=npm depName=markdownlint-cli2
MARKDOWNLINT_CLI2_VERSION=0.24.0

export NPM_CONFIG_UPDATE_NOTIFIER=false
npx --yes "markdownlint-cli2@$MARKDOWNLINT_CLI2_VERSION" "**/*.md"

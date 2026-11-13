#!/bin/sh
# The `build` check: the Dockerfile builds the image a deploy builds, with the build arguments the stack passes
# (yggdrasil's stacks/personal-blog.yml): the blog's address (blog.artur-rios.tech, at its root), the environment
# it deploys to (production, its only one) and the commit. Hugo runs inside it, with the theme the Dockerfile
# fetches, and the build fails when Hugo writes no site. Build only, no push and no run: the point is that the
# image can still be produced.
#
# yggdrasil.yml runs it in the pinned Docker CLI image (Alpine: no bash, so this is POSIX sh) with the CI engine's
# socket, from the repository's root. By hand, with your own engine:
#   docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v "$PWD:/src" -w /src <image from yggdrasil.yml> sh ci/build.sh
set -eu

# The repository's root, wherever this is run from.
cd "$(dirname "$0")/.."

# The commit, as deploy.sh passes it; empty where the checkout is not a git repository git can read.
commit=$(git -c safe.directory='*' rev-parse HEAD 2>/dev/null || true)

# A tag of this run's own (the container's hostname is its id): two builds at once never share one.
tag="personal-blog-check:$(hostname)"
# The image is only built to prove the Dockerfile works: remove it afterwards, whatever the outcome.
trap 'docker image rm --force "$tag" >/dev/null 2>&1 || true' EXIT

DOCKER_BUILDKIT=1 docker build --tag "$tag" \
  --build-arg PUBLIC_HOST=blog.artur-rios.tech \
  --build-arg PUBLIC_PATH= \
  --build-arg YGG_ENVIRONMENT=production \
  --build-arg GIT_COMMIT="$commit" \
  .

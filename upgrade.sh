#!/bin/sh
# upgrade.sh 1 2: upgrade from wchargin_platform_*1 to wchargin_platform_*2

set -eu
old="$1"
new="$2"
mv "main/wchargin_platform_main$old" "main/wchargin_platform_main$new"
for f in dep-*; do
    mv "$f/wchargin_platform_dep$old" "$f/wchargin_platform_dep$new"
done
find dep-* main \
    \( \( -name build -o -name dist -o -name '*.egg-info' \) -prune -false \) \
    -o -name '*.py' \
    -exec sed -i \
    -e "s/wchargin_platform_dep$old/wchargin_platform_dep$new/g" \
    -e "s/wchargin_platform_main$old/wchargin_platform_main$new/g" \
    {} +

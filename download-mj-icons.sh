#!/bin/bash
# Download all 30 Midjourney flat icons
# Run from ~/Fruityyyy: bash download-mj-icons.sh

mkdir -p mj-icons
cd mj-icons

JOBS=(
  "ddfd7286-6038-48f1-a314-403f1a695099"
  "abf3ba35-fc36-45db-a8ab-5abade51aa6e"
  "7382d5c2-acd3-45d8-a32c-dd496baabdb8"
  "76b85bd2-a4d1-4f2e-94c7-079dacbd7ea0"
  "e91d774b-7531-44be-a955-01b0fff6acd8"
  "7512d420-3a94-4a91-9eaf-74aed3fe16a5"
  "6d822f4b-69ff-4ca4-aafc-3774dc5e30f1"
  "d11a6960-648f-4d9f-aedb-49e58d9c6a45"
  "40c1f26b-0f0a-4ca1-be15-6b71293e870e"
  "e4a1afc3-5745-4904-b22c-9db278a94a63"
  "c8a4f673-0753-4510-b33b-fffd5bc9afab"
  "be027cb3-a831-4164-be5c-0b03c4d4293e"
  "fe605f14-f11f-4225-b43a-c05e33aff343"
  "63e52ebe-2889-4903-a218-3937daead7bd"
  "d9d8158b-b578-47fa-9ac4-43a0deda1d3f"
  "0121ac47-04a6-43b7-b0df-92a3f504eb95"
  "a6ebc186-1fc0-41e1-b7bc-8c875648f6d7"
  "992d2d32-140f-422e-8a14-5cb182d8e547"
  "2b84b530-e7f7-4968-bd87-a4fd8b6b1893"
  "fbe28a0f-64fb-463d-912e-524eb7930b88"
  "4028625f-5aff-4c21-a4ed-957996783b7c"
  "5febb46d-fb85-4a27-8cbe-be8992813b31"
  "79f040b9-b971-45a8-aba3-514e5040a61a"
  "20a9d426-ef55-4626-8978-c35886c51aef"
  "6bf58e35-c91a-4fda-bea9-e319fb478c83"
  "1a39a624-1aba-40b4-99c5-636745cef070"
  "aff20b47-203e-4ce4-beb0-fd291e5088d8"
  "18765378-0762-44e8-8670-807229306ed9"
  "bc7f26dd-00de-4854-976f-ba41fab26c85"
  "695f884c-766a-43b0-8096-6c4c7d685253"
)

echo "Downloading ${#JOBS[@]} Midjourney icons..."
i=1
for JOB in "${JOBS[@]}"; do
  PADDED=$(printf "%02d" $i)
  echo "[$PADDED/${#JOBS[@]}] Downloading ${JOB:0:8}..."
  curl -s -o "icon-${PADDED}-${JOB:0:8}.webp" "https://cdn.midjourney.com/${JOB}/0_0.webp"
  i=$((i + 1))
done

echo ""
echo "Done! Downloaded $(ls *.webp 2>/dev/null | wc -l) icons to mj-icons/"
ls -lh *.webp

name: Apply v0.5.4 fixes
on:
  workflow_dispatch:
    inputs:
      file:
        description: HTML file to patch
        default: index.html
permissions:
  contents: write
jobs:
  patch:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.x"
      - name: Run patch
        run: python fix_care_a_garden.py "${{ inputs.file }}"
      - name: Commit to a new branch
        run: |
          rm -f "${{ inputs.file }}.bak"
          git config user.name "github-actions"
          git config user.email "github-actions@users.noreply.github.com"
          git checkout -b fix-v0.5.4
          git add "${{ inputs.file }}"
          git commit -m "Fix Care a Garden v0.5.4 bugs"
          git push origin fix-v0.5.4

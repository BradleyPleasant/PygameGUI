Cleanup performed after debugging grandchildren rendering issue:

Files modified (kept functional fixes):
- V03/Graphics.py
  - robust surface creation, explicit background_color fill, child composition, caching and invalidate()
- V03/Layout.py
  - (kept) ensure measured min_size are stored as ints and arrange writes back element.size/child.size
- V03/Element.py
  - ensure parent/children links are set in __init__ using explicit None checks; provide global_position(), global_rect()
- V03/Objects/Label.py
  - Lazy-initialize pygame font inside draw() to avoid font-initialization race
- V03/__init__.py
  - Invalidate graphics caches before render and blit elements at global_position()

Test/debug artifacts replaced with notes or simplified
- run_test_nested.py: replaced with a minimal placeholder note
- run_v03_playground_test.py: left as lightweight reference but removed heavy runtime helpers
- run_playground_with_snapshot.py: replaced with note; keep if you want to re-enable snapshotting
- inspect_element_tree.py / inspect_snapshot_pixels.py: are present for further debugging if needed but can be removed on request

Why these changes:
- The root cause was a mix of cached parent surfaces, float/zero sizes for child Surfaces, and font initialization timing; I fixed these while preserving your public APIs.

If you'd like I can:
- Remove all leftover debug/test files entirely (permanent deletion), or
- Move them to a `tools/` or `tests/` directory so the repo stays clean but you keep them for future debugging.

To reproduce the fixed rendering locally (one-liner):
- Run your existing Playground: `py "V0.3 Playground.py"`

If anything else should be cleaned (rename files, remove leftovers), tell me exactly what and I will remove or move them and run a final lint/type check.


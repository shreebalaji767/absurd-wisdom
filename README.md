# The Human Wisdom Archive

A static, browser-based archive of strange observations, practical philosophy, human behavior, ordinary problems, and unusually logical absurdity.

The presentation is designed as a formal archival repository. The observations themselves may be chaotic, humorous, unexpected, or absurd while remaining internally coherent.

## Features

- Static website
- Python-powered build generation
- No database
- No backend database
- No login
- No signup
- No user accounts
- No server-side user data
- Browser-only record history
- No repeated record on the same browser until the available combination space is exhausted
- Responsive design
- Desktop, tablet, and mobile support
- Copy Quote
- Copy Quote + Author
- Copy full record
- Screenshot Quote
- Print support
- English / Hindi interface
- Keyboard shortcut for generating a new record
- Large combinatorial record pool
- Formal archival presentation
- Works as a static site after generation

## How It Works

The project uses Python to generate the static `index.html` file.

The generated page contains the archive data and browser-side JavaScript.

The browser then creates records locally.

The basic process is:

1. `generate.py` is executed.
2. `index.html` is generated.
3. The static site is served.
4. JavaScript selects a record.
5. The browser checks its local archive history.
6. Previously seen records are excluded.
7. A new record is displayed.
8. The record identifier is saved in browser storage.
9. Refreshing the page selects another unseen record.

There is no database involved.

## Browser Memory

The project uses browser `localStorage` for the no-repeat system.

The storage key is:

```text
human_wisdom_archive_seen_v3

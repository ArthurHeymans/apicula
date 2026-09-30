# NORbert experimental database

The `norbert-experimental` integration branch ships `apycula/GW5A-25A.msgpack.xz`
so the pinned open-source toolchain does not need a Gowin installation to build.
The generated database is intentionally absent from the upstream topic branches.
Only GW5A-25A is packaged by this integration branch.

SHA-256: `a5f9153446566c2217ce3c450a7889e2bc0fe823409d8f4759160951989cf7f2`

This is the cached database from the local GW5A experiments, not a freshly
regenerated database. It contains the `HAS_5A_IOREG` flag, the CE0/IOLOGICCE0
ports and 2880 RAM16-capable grid tiles. The integration tests check these
capabilities. Raw vendor input files are not distributed.

Apicula's `GWVERSION` specifies Gowin 1.9.10.03. Regeneration attempted with
Gowin Education 1.9.11.03 failed in `fse_parser.read_fse`; do not use that version
to regenerate this artifact without first addressing the format difference.
The vendor input version of this cached artifact has not been independently
re-established. A reproducible regeneration is still required before treating
the hardware-support branches as ready for upstream acceptance.

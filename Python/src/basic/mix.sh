# regress test 1
cat parallel_schedule0 >> mix
cat Mogdb_copy_schedule >> mix
cat Mogdb_compression_schedule >> mix
cat Mogdb_reidx_concurrently_schedule >> mix
cat Mogdb_compatibility_oracle_schedule >> mix
# regress test 2
cat parallel_schedule0C >> mix
cat Mogdb_regress_enhancement >> mix
cat parallel_schedule15 >> mix
cat parallel_schedule066 >> mix
cat parallel_schedule6 >> mix
cat parallel_schedule11 >> mix
cat parallel_schedule12 >> mix
cat MogDB_compression_table_parallel_schedule0 >> mix

sed '/^#.* /d' mix |  tr -s ' ' '\n'|sort|uniq -c |sort -r|awk '{if($1 > 1){print $2" "$1}}'
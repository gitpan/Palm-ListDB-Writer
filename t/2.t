use strict;
use warnings;
use Test::More tests => 5;

-d "t" && chdir("t");
ok(eval { require "dbcmp.pl" }, "require dbcmp.pl");

my @dels = qw(2.pdb);
unlink(@dels);

ok(!system("../blib/script/csv2lsdb --pdb=2.pdb 2.dat"));

dbcmp("2.pdb", "1.ref", 648) && unlink(@dels);

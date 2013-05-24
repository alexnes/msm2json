package Avtobus::MSMCmd;

use Exporter;
@ISA = qw(Exporter);
@EXPORT = qw( CmdMsm
                dostokoi koitodos koitowin wintokoi
                MsgToWebmaster
            );

use strict;

sub CmdMsm{
my $p=shift || 'w '; return koitodos('MSMshell ' . $p);
}

sub dostokoi {
    my $pvdcoderdos=shift;
   $pvdcoderdos=~ tr 
/\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff
/\341\342\367\347\344\345\366\372\351\352\353\354\355\356\357\360\362\363\364\365\346\350\343\376\373\375\377\371\370\374\340\361\301\302\327\307\304\305\326\332\311\312\313\314\315\316\317\320\220\221\222\xb3\207\262\234\230\231\265\241\250\256\237\254\203\204\211\210\206\200\212\257\260\253\245\273\270\261\240\276\271\272\223\233\252\251\242\225\227\274\205\202\215\214\216\217\213\322\323\324\325\306\310\303\336\333\335\337\331\330\334\300\321\263\243\xbd\xad\xb4\xa4\xb2\246\267\247\236\226\277\235\224\232
/;
return $pvdcoderdos;
}        

sub koitodos {
    my $pvdcoderdos=shift;
   $pvdcoderdos=~ tr/
\341\342\367\347\344\345\366\372\351\352\353\354\355\356\357\360\362\363\364\365\346\350\343\376\373\375\377\371\370\374\340\361\301\302\327\307\304\305\326\332\311\312\313\314\315\316\317\320\220\221\222\201\207\262\234\230\231\265\241\250\256\237\254\203\204\211\210\206\200\212\257\260\253\245\273\270\261\240\276\271\272\223\233\252\251\242\225\227\274\205\202\215\214\216\217\213\322\323\324\325\306\310\303\336\333\335\337\331\330\334\300\321\263\243\275\255\264\244\266\246\267\247\236\226\277\235\224\232/
\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff/
;
return $pvdcoderdos;
}        

sub koitowin {
    my $pvdcoderwin=shift;
    $pvdcoderwin=~ tr
/\xE1\xE2\xF7\xE7\xE4\xE5\xF6\xFA\xE9\xEA\xEB\xEC\xED\xEE\xEF\xF0\xF2\xF3\xF4\xF5\xE6\xE8\xE3\xFE\xFB\xFD\xFF\xF9\xF8\xFC\xE0\xF1\xC1\xC2\xD7\xC7\xC4\xC5\xD6\xDA\xC9\xCA\xCB\xCC\xCD\xCE\xCF\xD0\xD2\xD3\xD4\xD5\xC6\xC8\xC3\xDE\xDB\xDD\xDF\xD9\xD8\xDC\xC0\xD1\xad\xbd\xa4\xb4
/\xC0\xC1\xC2\xC3\xC4\xC5\xC6\xC7\xC8\xC9\xCA\xCB\xCC\xCD\xCE\xCF\xD0\xD1\xD2\xD3\xD4\xD5\xD6\xD7\xD8\xD9\xDA\xDB\xDC\xDD\xDE\xDF\xE0\xE1\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xEB\xEC\xED\xEE\xEF\xF0\xF1\xF2\xF3\xF4\xF5\xF6\xF7\xF8\xF9\xFA\xFB\xFC\xFD\xFE\xFF\xbd\xaa\xbf\xaf
/;
return $pvdcoderwin;
}

sub wintokoi {
    my $pvdcoderwin=shift;
    $pvdcoderwin=~ tr/\xC0\xC1\xC2\xC3\xC4\xC5\xC6\xC7\xC8\xC9\xCA\xCB\xCC\xCD\xCE\xCF\xD0\xD1\xD2\xD3\xD4\xD5\xD6\xD7\xD8\xD9\xDA\xDB\xDC\xDD\xDE\xDF\xE0\xE1\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xEB\xEC\xED\xEE\xEF\xF0\xF1\xF2\xF3\xF4\xF5\xF6\xF7\xF8\xF9\xFA\xFB\xFC\xFD\xFE\xFF/\xE1\xE2\xF7\xE7\xE4\xE5\xF6\xFA\xE9\xEA\xEB\xEC\xED\xEE\xEF\xF0\xF2\xF3\xF4\xF5\xE6\xE8\xE3\xFE\xFB\xFD\xFF\xF9\xF8\xFC\xE0\xF1\xC1\xC2\xD7\xC7\xC4\xC5\xD6\xDA\xC9\xCA\xCB\xCC\xCD\xCE\xCF\xD0\xD2\xD3\xD4\xD5\xC6\xC8\xC3\xDE\xDB\xDD\xDF\xD9\xD8\xDC\xC0\xD1/;
return $pvdcoderwin;
}


sub MsgToWebmaster {
       my ($text,$subj,$to,$from) ;
   $text = shift;
   $subj = shift;
   $to = shift;
   $from = shift;

   $text = '' unless $text ; 
   $subj = '' unless $subj ;
   $to = '' unless $to     ;
   $from = '' unless $from ;
   chomp $from ;
   chomp $to ;
   chomp $subj ;

   my $TimeShatmp = localtime();
print STDERR <<EOF
$TimeShatmp
$from
$to
$subj
$text
EOF
;
}

1;

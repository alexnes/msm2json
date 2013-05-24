#!/usr/bin/perl -w
#Выполнить команды МСМ (каждая в синтаксисе МСМ и отдельным параметром)

use strict;
use IO::Socket;
use Fcntl qw(:DEFAULT :flock);

use Avtobus::MSMCmd;

for (@ARGV){

                                #синхронизация
   open(LOCK,'>/tmp/5050.lock');
   flock(LOCK,LOCK_EX) ; print LOCK "$$\n"; 
   unlink('/tmp/5050.lock');
   
my $cnt = IO::Socket::INET->new(Proto => "tcp",PeerAddr => "192.168.20.2",PeerPort => '5050', Timeout => 10) 
			|| die "Can't connect to server: $!";        
   $cnt->autoflush(1);        


#my $cnt = IO::Socket::INET->new(Proto => "tcp",PeerAddr => "localhost",PeerPort => '5050') 
#			|| die "Can't connect to server: $!";        
#    $cnt->autoflush(1);        
    
    print $cnt &CmdMsm($_) ;
    while ( <$cnt> ) {
        print dostokoi($_)
    }
}
exit 0;


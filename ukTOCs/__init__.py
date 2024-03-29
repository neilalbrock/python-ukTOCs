# coding: utf-8
from collections import namedtuple

__all__ = ["tocs"]

TOC = namedtuple('TOC', 'code, name, url')

_records = [
    TOC('AW',u'ARRIVA Trains Wales',u'http://www.arriva.co.uk'),
    TOC('CC',u'c2c',u'http://www.c2c-online.co.uk'),
    TOC('CH',u'Chiltern Railway Co.',u'http://www.chilternrailways.co.uk'),
    TOC('XC',u'CrossCountry',u'http://www.crosscountrytrains.co.uk'),
    TOC('GR',u'East Coast',u'http://www.eastcoast.co.uk'),
    TOC('EM',u'East Midlands Trains',u'http://www.eastmidlandstrains.co.uk'),
    TOC('ES',u'Eurostar',u'http://www.eurostar.com'),
    TOC('FC',u'First Capital Connect',u'http://www.firstcapitalconnect.co.uk'),
    TOC('GW',u'First Great Western',u'http://www.firstgreatwestern.com'),
    TOC('HT',u'First Hull Trains',u'http://www.hulltrains.co.uk'),
    TOC('TP',u'First TransPennine Express',u'http://www.tpexpress.co.uk'),
    TOC('GC',u'Grand Central',u'http://www.grandcentralrail.com'),
    TOC('LE',u'Greater Anglia',u'http://www.greateranglia.co.uk'),
    TOC('HX',u'Heathrow Express',u'http://www.heathrowexpress.com'),
    TOC('LM',u'London Midland',u'http://www.londonmidland.com'),
    TOC('LO',u'London Overground',u'http://www.lorol.co.uk'),
    TOC('ME',u'Merseyrail',u'http://www.merseyrail.org'),
    TOC('NT',u'Northern',u'http://www.northernrail.org'),
    TOC('SR',u'ScotRail',u'http://www.scotrail.co.uk'),
    TOC('SN',u'Southern',u'http://www.southernrailway.com'),
    TOC('SE',u'Southeastern',u'http://www.southeasternrailway.co.uk'),
    TOC('SW',u'South West Trains',u'http://www.southwesttrains.co.uk'),
    TOC('VT',u'Virgin Trains',u'http://www.virgintrains.co.uk'),
    TOC('HC',u'Heathrow Connect',u'http://www.heathrowconnect.com'),
    TOC('GX',u'Gatwick Express',u'http://www.gatwickexpress.com'),
    TOC('LT',u'London Underground',u'http://tube.tfl.gov.uk'),
    TOC('IL',u'Island Line',u'http://www.southwesttrains.co.uk'),
    TOC('SX',u'Stansted Express','https://www.stanstedexpress.com/'),
    TOC('NY',u'North Yorkshire Moors Railway',u'http://www.nymr.co.uk'),
    TOC('WR',u'West Coast Railway Co.',u'http://www.westcoastrailways.co.uk'),
    TOC('TW',u'Tyne and Wear Metro',u'http://www.nexus.org.uk/metro'),
    TOC('ZZ',u'Unknown',u'')]

def _build_index(idx):
    return dict((r[idx], r) for r in _records)

_by_code = _build_index(0)

class _TOCLookup(object):

    def get (self, key):        
        k = key.upper()
        if len(k) == 2:
            return _by_code[k]        
        raise ValueError()
    
    def __iter__(self):
        return iter(_records)

tocs = _TOCLookup()
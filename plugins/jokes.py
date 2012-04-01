#!/usr/bin/python
# -*- coding: utf-8 -*-


from plugin import *
import feedparser
import htmlentitydefs
import re

from siriObjects.uiObjects import AddViews, AssistantUtteranceView


class jokes(Plugin):
    @register("fr-FR", "(Blague)|(Humour.*)")
    def joke_du_Matin(self, speech, language):
        if  language == 'fr-FR':
            rss = "http://blague.dumatin.fr/blagues.xml"

        feeds = feedparser.parse(rss)
        NomBlague = feeds.entries[0]['title']
        Blague = feeds.entries[0].description        
        TxtBlagueSansCaractere = Blague.replace("<br />","")
        TxtBlague = TxtBlagueSansCaractere[0:TxtBlagueSansCaractere.index("<a href=")]
        LienSite = TxtBlagueSansCaractere[TxtBlagueSansCaractere.index("<a href=") + 8]
        print LienSite
        if language == 'fr-FR':
            view = AddViews(self.refId, dialogPhase="Summary")
            view1 = AssistantUtteranceView(text=TxtBlague, speakableText="Voici une blague du matin", dialogIdentifier="Blague#created")
            view.views = [view1]
            self.sendRequestWithoutAnswer(view)
        self.complete_request()

    @register("de-DE", "(.*Hallo.*)|(.*Hi.*Siri.*)")
    @register("en-US", "(.*Hello.*)|(.*Hi.*Siri.*)")
    @register("fr-FR", "(Bonjour)|(Salut)")
    def rep_bonjour(self, speech, language):
        print language
        if language == 'de-DE':
            self.say("Hallo.")
        elif language == 'en-US':
            self.say("Hello")
        elif language == 'fr-FR':
            self.say("Bonjour, comment ca va aujourd'hui ?")
        self.complete_request()

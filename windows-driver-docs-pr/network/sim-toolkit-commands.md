---
title: SIM toolkit commands
description: SIM toolkit commands
ms.assetid: 7c13c27a-7a2d-4eae-a64e-1133aa533343
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SIM toolkit commands


The following SIM toolkit commands are supported unless otherwise noted.

## Display text


DISPLAY TEXT, Normal priority, unpacked 8 bit data for Text String

DISPLAY TEXT, High priority, unpacked 8 bit data for Text String

DISPLAY TEXT, Packed, SMS default alphabet

DISPLAY TEXT, Clear message after delay

DISPLAY TEXT, Text string with 160 bytes

DISPLAY TEXT, Backward move in UICC session

DISPLAY TEXT, Session terminated by user

DISPLAY TEXT, No response from user

DISPLAY TEXT, Display of the extension text

DISPLAY TEXT, Sustained text, unpacked data 8 bits

DISPLAY TEXT, Sustained text, clear message after delay

DISPLAY TEXT, Sustained text, wait for user MMI to clear

DISPLAY TEXT, Variable time-out of 10 seconds

DISPLAY TEXT, UCS2 coded—Chinese characters

DISPLAY TEXT, UCS2 coded—Katakana characters

## Get inkey


GET INKEY, Digits only for character set, unpacked 8 bit data for Text String

GET INKEY, Digits only for character set, SMS default Alphabet for Text String

GET INKEY, Backward move

GET INKEY, Abort

GET INKEY, SMS default alphabet for character set; unpacked 8 bit data for Text String

GET INKEY, Max length for the Text String

GET INKEY, No response from the user

GET INKEY, "Yes/No" Response for the input

GET INKEY, Help information available

GET INKEY, Variable time out of 10 seconds

GET INKEY, Text string coding in UCS2 Alphabet, successful

GET INKEY, Max length for the Text String coding in UCS2 Alphabet, successful

GET INKEY, Characters from UCS2 alphabet, successful

GET INKEY, Text string coding in UCS2 Alphabet—Chinese characters, successful

GET INKEY, Characters from UCS2 alphabet—Chinese characters, successful

GET INKEY, Text string coding in UCS2 Alphabet—Katakana characters, successful

GET INKEY, Max length for the Text String coding in UCS2 Alphabet—Katakana characters, successful

GET INKEY, Characters from UCS2 alphabet—Katakana characters, successful

## Get input


GET INPUT, Digits only, SMS default alphabet, ME to echo text, ME supporting 8 bit data message

GET INPUT, Digits only, SMS default alphabet, ME to echo text, packing SMS Point-to-point required by ME

GET INPUT, Character set, SMS default alphabet, ME to echo text, ME supporting 8 bit data message

GET INPUT, Digits only, SMS default alphabet, ME to hide text, ME supporting 8 bit data Message

GET INPUT, Digits only, SMS default alphabet, ME to echo text, ME supporting 8 bit data Message, 20 digits

GET INPUT, Backwards move

GET INPUT, Abort

GET INPUT, Digits only, SMS default alphabet, ME to echo text, ME supporting 8 bit data Message, 160 digits

GET INPUT, Digits only, SMS default alphabet, ME to echo text, ME supporting 8 bit data Message, no input

GET INPUT, Null length for the text string, successful

GET INPUT, No response from the user

GET INPUT, Default text for the input, successful

GET INPUT, Default text for the input with max length, successful

GET INPUT, Text string coding in UCS2, successful

GET INPUT, Max length for the text string coding in UCS2, successful

GET INPUT, Character set from UCS2 alphabet, successful

GET INPUT, Character set from UCS2 alphabet, Max length for the input, successful

## More time


MORE TIME

## Play tone


PLAY TONE

PLAY TONE, Character set from UCS2 alphabet, successful

PLAY TONE, Character set from UCS2 alphabet in Chinese, successful

PLAY TONE, With UCS2 in Katakana, successful

## Poll interval


POLL INTERVAL, 20 Seconds

POLL INTERVAL, POLLING OFF \[Status commands are sent again after a call\]

## Provide local information


PROVIDE LOCAL INFORMATION, Location Information (MCC, MNC, LAC and Cell ID)

PROVIDE LOCAL INFORMATION, IMEI of the ME

PROVIDE LOCAL INFORMATION, Network Measurement Results (NMR)

PROVIDE LOCAL INFORMATION, Date, Time, Time Zone \[Needs OEM NVRAM setting\]

PROVIDE LOCAL INFORMATION, Language setting

PROVIDE LOCAL INFORMATION, Timing Advance

PROVIDE LOCAL INFORMATION, Access Technology

PROVIDE LOCAL INFORMATION, IMEISV \[Needs OEM NVRAM setting\]

<strong>\\</strong>*PROVIDE LOCAL INFORMATION, Search Mode information—Network search mode **\*\*Not supported\*\\***

PROVIDE LOCAL INFORMATION, Intra-Frequency UTRAN Measurements

PROVIDE LOCAL INFORMATION, Inter-frequency UTRAN Measurements

## Refresh


REFRESH, USIM Initialization

REFRESH, File Change Notification

REFRESH, USIM Initialization and File Change Notification

REFRESH, USIM Initialization and Full File Change Notification

REFRESH, UICC Reset

REFRESH, USIM Initialization after SMS-PP data download

REFRESH, USIM Application Reset

REFRESH, UICC Reset for IMSI Changing procedure

REFRESH, USIM Application Reset for IMSI Changing procedure

REFRESH, 3G Session Reset for IMSI Changing procedure

REFRESH, Reject 3G Session Reset for IMSI Changing procedure during call

REFRESH, Steering of roaming, UTRAN

REFRESH, Steering of roaming, InterRAT

## Select item


SELECT ITEM, Mandatory features, successful

SELECT ITEM, Large menu, successful

SELECT ITEM, Call options, successful

SELECT ITEM, Backward move by user, successful

SELECT ITEM, "Y", successful

SELECT ITEM, Large menu, successful

SELECT ITEM, Default item, successful

SELECT ITEM, No response from user

SELECT ITEM, With UCS2 in Cyrillic characters, 0x80 UCS2 coding, successful

SELECT ITEM, With UCS2 in Cyrillic characters, 0x81 UCS2 coding, successful

SELECT ITEM, With UCS2 in Cyrillic characters, 0x82 UCS2 coding, successful

SELECT ITEM, With UCS2 in Chinese characters, successful

SELECT ITEM, With UCS2 in Katakana characters, 0x80 UCS2 coding, successful

SELECT ITEM, With UCS2—Katakana characters, 0x81 UCS2 coding, successful

SELECT ITEM, With UCS2—Katakana characters, 0x82 UCS2 coding, successful

SELECT ITEM, Next action indicator, successful

## Send DTMF


SEND DTMF, with Alpha Id normal

SEND DTMF, containing alpha identifier

SEND DTMF, Mobile is not in a speech call with no Alpha Id

SEND DTMF, UCS2 text in Chinese, successful

SEND DTMF, UCS2 text in Katakana, successful

## Send short message


SEND SHORT MESSAGE, Packing not required, 8 bit data

SEND SHORT MESSAGE, Packing required, 8 bit data

SEND SHORT MESSAGE, Packing required, without SMS-Center address, 8 bit data

SEND SHORT MESSAGE, Packing required, message of 160 bytes, 8 bit data

SEND SHORT MESSAGE, Packing not required, SMS default alphabet, message of 160 bytes

SEND SHORT MESSAGE, Packing not required, UCS2 (16-bit data)

SEND SHORT MESSAGE, alpha identifier 160 bytes long, SMS default alphabet, successful

SEND SHORT MESSAGE, Packing not required, alpha identifier length ‘00’, 8-bit data, successful

SEND SHORT MESSAGE, Packing not required, 8-bit data, no alpha identifier, successful

## Send SS


SEND SS, call forward unconditional, all bearers, successful

SEND SS, call forward unconditional, all bearers, Return Error **\*\*Not fully verified\*\\***

SEND SS, call forward unconditional, all bearers, Reject

SEND SS, call forward unconditional, Large SS string

SEND SS, interrogate CLIR status, successful, alpha identifier limits

SEND SS, with Null Alpha Id (Activate Call Forwarding to international number)

SEND SS, UCS2 support

SEND SS, Call forward unconditional, all bearers, successful, UCS2 text in Chinese

SEND SS, Call forward unconditional, all bearers, successful, UCS2 text in Katakana

## Send USSD


SEND USSD, 7-bit data, with Alpha ID

SEND USSD, 8-bit data, with Alpha ID

SEND USSD, UCS2 data, with Alpha ID

SEND USSD, 7-bit data, unsuccessful (Return Error)

SEND USSD, 7-bit data, unsuccessful (Reject)

SEND USSD, 7-bit data, with large Alpha ID, 256 characters

SEND USSD, 7-bit data, with no Alpha ID

SEND USSD, 7-bit data, with null Alpha ID

## Set up call


SET UP CALL, call confirmed by the user and connected

SET UP CALL, call rejected by the user

SET UP CALL, putting all other calls on hold, ME busy

SET UP CALL, disconnecting all other calls, ME busy

SET UP CALL, only if not currently busy on another call, ME busy

SET UP CALL, putting all other calls on hold, call hold is not allowed

SET UP CALL, max dialing number string, no alpha identifier

SET UP CALL, 256 bytes length, long first alpha identifier

SET UP CALL, Called party sub-address

SET UP CALL, Maximum duration for the redial mechanism

## Set up event list


SET UP EVENT LIST, Set Up Call Connect Event

SET UP EVENT LIST, Replace Event

SET UP EVENT LIST, Remove Event

SET UP EVENT LIST, Remove Event on ME Power Cycle

## Set up menu


SET UP MENU and MENU SELECTION, without Help Request, Replace and Remove a Toolkit Menu

SET UP MENU, Large Menu with many items or with large items or with Large Alpha Identifier

SET UP MENU and MENU SELECTION, with Help Request, Replace and Remove a Toolkit Menu

SET UP MENU, next action indicator "Send SM", "Set Up Call", "Launch Browser", "Provide Local Information", successful

SET UP MENU and MENU SELECTION, without Help Request, Replace and Remove a Toolkit Menu, with UCS2 in Cyrillic Characters

SET UP MENU and MENU SELECTION, without Help Request, Replace and Remove a Toolkit Menu, with UCS2 in Chinese Characters

SET UP MENU and MENU SELECTION, without Help Request, Replace and Remove a Toolkit Menu, with UCS2 in Katakana Characters

## Timer management


TIMER MANAGEMENT, Start timer 1, get the current value of the timer and deactivate the timer

TIMER MANAGEMENT, Start timer 2, get the current value of the timer and deactivate the timer

TIMER MANAGEMENT, Start timer 8, get the current value of the timer and deactivate the timer

TIMER MANAGEMENT, Try to get the current value of a timer which is not started

TIMER MANAGEMENT, Try to deactivate a timer which is not started

TIMER MANAGEMENT, Start 8 timers

## Call control by USIM


CALL CONTROL BY USIM, set up call attempt by user, the USIM responds with '90 00'

CALL CONTROL BY USIM, set up call attempt by user, allowed without modification

CALL CONTROL BY USIM, set up call attempt resulting from a set up call proactive command, allowed without modification

CALL CONTROL BY USIM, set up call attempt by user, not allowed

CALL CONTROL BY USIM without ALPHA ID, set up call attempt resulting from a set up call proactive command, not allowed

CALL CONTROL BY USIM without ALPHA ID, set up call attempt by user, allowed with modifications

CALL CONTROL BY USIM without ALPHA ID, set up call attempt resulting from a set up call proactive command, allowed with modifications

CALL CONTROL BY USIM, set up call attempt by user, allowed with modifications: emergency call

CALL CONTROL BY USIM, set up call attempt by user, allowed with modifications: number in EFECC

CALL CONTROL BY USIM, set up call attempt by user to an emergency call

CALL CONTROL BY USIM, set up call through call register, the USIM responds with '90 00'

CALL CONTROL BY USIM, set up call through call register, allowed without modification

CALL CONTROL BY USIM, set up call through call register, not allowed

CALL CONTROL BY USIM, set up call through call register, allowed with modifications

CALL CONTROL BY USIM, send SS, the USIM responds with '90 00'

CALL CONTROL BY USIM, send SS, allowed without modifications

CALL CONTROL BY USIM, send SS, not allowed

CALL CONTROL BY USIM, send SS, allowed with modifications

CALL CONTROL BY USIM, set up a call NOT in EF FDN

CALL CONTROL BY USIM, set up a call in EF FDN, the USIM responds with '90 00'

CALL CONTROL BY USIM, set up a call in EF FDN, Allowed without modifications

CALL CONTROL BY USIM, set up a call in EF FDN, Not Allowed

CALL CONTROL BY USIM, set up a call in EF FDN, Allowed with modifications

## MS SM control by USIM


MO SM CONTROL BY USIM, with Proactive command, Allowed, no modification

MO SM CONTROL BY USIM, with user SMS, Allowed, no modification

MO SM CONTROL BY USIM, with Proactive command, Not allowed

MO SM CONTROL BY USIM, with user SMS, Not allowed

MO SM CONTROL BY USIM, with Proactive command, Allowed with modifications

MO SM CONTROL BY USIM, with user SMS, Allowed with Modifications

## Envelope timer expiration


ENVELOPE TIMER EXPIRATION, from Timer Management: pending proactive UICC command

ENVELOPE TIMER EXPIRATION, from Timer Management: UICC application toolkit busy

## Event download


EVENT DOWNLOAD, Call Connected

EVENT DOWNLOAD, Call connected, ME supporting SET UP CALL

EVENT DOWNLOAD, Call Disconnected

EVENT DOWNLOAD LOCATION STATUS

EVENT DOWNLOAD MT CALL

EVENT DOWNLOAD, USER ACTIVITY

EVENT DOWNLOAD, Data available, GPRS

EVENT DOWNLOAD, Channel Status on a link dropped

**\\**<em>EVENT DOWNLOAD, Network Search Mode Change Event</em>*\*\*Not supported\*\***

## Open channel


OPEN CHANNEL, immediate link establishment, GPRS, no local address, no alpha identifier, no network access name

OPEN CHANNEL, immediate link establishment, GPRS, no local address, no alpha identifier, with network access name

OPEN CHANNEL, immediate link establishment, GPRS, with alpha identifier

OPEN CHANNEL, immediate link establishment, GPRS, with null alpha identifier

OPEN CHANNEL, immediate link establishment, GPRS, command performed with modifications (buffer size)

OPEN CHANNEL, immediate link establishment, GPRS, with alpha identifier, user did not accept the proactive command

## Get channel status


GET STATUS, without any BIP channel opened

GET STATUS, with a BIP channel currently opened

GET STATUS, after a link dropped

## Send data


SEND DATA, immediate mode

SEND DATA, store mode

SEND DATA, 2 consecutive SEND DATA commands in store mode

SEND DATA, Store mode, Tx buffer fully used

SEND DATA, with Alpha ID, Store mode, Tx buffer fully used

SEND DATA, immediate mode with a bad channel identifier

## Receive data


RECEIVE DATA, already opened channel

## Close channel


CLOSE CHANNEL, successful

CLOSE CHANNEL, with an invalid channel identifier

CLOSE CHANNEL, on an already closed channel

## Terminal profile


TERMINAL PROFILE, 3GPP

TERMINAL PROFILE, Microsoft Requirements

## SMS–PP


SMS PP, UICC responds with "61XX" (acknowledgement)

SMS PP, More Time

SMS PP, Data coding/ Message class

SMS PP, GDC UDH

SMS PP, Concatenated SMS 8 bit reference number

SMS PP, USIM security header

## BIP download


BIP UDP download, 3G, browse menu

BIP TCP download, 3G, incoming call

BIP UDP download, 2G, incoming call

<strong>\\</strong>*BIP Download, lost network during download **\*\*Not supported\*\\***

## SMS CB


**Note**  
The OEM must modify and enable SMS providers for cell broadcast

 

SMS CB, No display

<strong>\\</strong>*SMS CB, Display **\*\*Not supported\*\\***

## Related topics


[SIM toolkit](sim-toolkit.md)

 

 







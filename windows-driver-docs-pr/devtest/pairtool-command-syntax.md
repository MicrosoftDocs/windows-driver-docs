---
title: PairTool command syntax
description: How to run PairTool, including syntax and parameters.
ms.date: 10/31/2023
prerelease: true
---

# PairTool command syntax

To run PairTool, open a command prompt window and type a command using the following syntax and commands.

``` cmd
pairtool [/enum-endpoints <...> | /enum-services <...> | /enum-containers <...> | 
          /enum-protocols <...> | /associate <...> | /associate-oob <...> | 
          /disassociate <...> | /challenge <...> | /?] 
```

## /enum-endpoints

Enumerates device endpoints over the various protocols Windows supports. Examples of endpoints: wireless headset, network printer, or TV.

```syntax
  /enum-endpoints [/protocol <protocol1>[,<protocol2>[,...]] [/persisted]
                  [/sync] [/instance <id1>[,<id2>[,...]] [/url <url>]] 
                  [/continuous] [/format <txt | xml | csv>] 
                  [/output-file <filename>] 
```

Flags:

- `/protocol` - Protocol(s) to discover with. More than one protocol may be comma separated. Possible protocols may be enumerated with the /enum-protocols. The protocol ID or class are acceptable inputs here.

- `/persisted` - Enumerate endpoints persisted in the OS. This option will not initiate over-the-wire discovery.

- `/sync` - Hold results until fully enumerated. This is not recommended as it can take a long time to get any results. Many protocols don't support the concept of "fully enumerated," so these protocols use long timeouts are used instead.

- `/instance` - Endpoint instance(s) to discover directly. More than one instance ID may be comma separated. This allows for what some protocols describe as "directed discovery."

- `/continuous` - Continue enumerating until Ctrl+C is pressed.

- `/url` - Update PNPX remote address for directed discovery.

- `/format` - Output format. Valid options are `txt`, `xml`, or `csv`.

- `/output-file` - Output file.

## /enum-services

Enumerates device endpoint services over the various protocols Windows supports. Examples of endpoint services: Bluetooth GATT, UPnP Digital Media Renderer (DMR), or ESCL scanning.

```syntax
  /enum-services [/protocol <protocol1>[,<protocol2>[,...]] [/persisted] [/sync]
                 [/instance <id1>[,<id2>[,...]] [/continuous] 
                 [/format <txt | xml | csv>] [/output-file <filename>] 
```

Flags:

- `/protocol` - Protocol(s) to discover with. More than one protocol may be comma separated.

- `/sync` - Hold results until fully enumerated. This is not recommended as it can take a long time to get any results. Many protocols don't support the fully enumerated concept, so these protocols use long timeouts instead.

- `/instance` - Directed discovery of a specific service instance(s). More than one instance ID may be comma separated.

- `/continuous` - Continue enumerating until Ctrl+C is pressed.

- /format - Output format as text, XML, or CSV. Valid options are `txt`, `xml`, or `csv`.

- `/output-file` - Output file.

## /enum-containers

Enumerates device endpoint containers over the various protocols Windows supports. Examples of endpoint containers: an XBOX on your network, an NAS, or a smart TV.

```syntax
  /enum-containers [/protocol <protocol1>[,<protocol2>[,...]] [/persisted]
                   [/sync] [/instance <id1>[,<id2>[,...]] [/continuous] 
                   [/format <txt | xml | csv>] [/output-file <filename>] 
```

Flags:

- `/protocol` - Protocol(s) to discover with. More than one protocol may be comma separated.

- `/sync` - Hold results until fully enumerated. This is not recommended as it can take a long time to get any results. Many protocols don't support the fully enumerated concept, so these protocols use long timeouts are used instead.

- `/instance` - Directed discovery of specific container instances.

- `/continuous` - Continue enumerating until Ctrl+C is pressed.

- `/format` - Output format as text, XML, or CSV. Valid options are `txt`, `xml`, or `csv`.

- `/output-file` - Output file.

## /enum-protocols

Enumerates protocols supported in the OS this tool is running on.

  /enum-protocols [/format <txt | xml | csv>] [/output-file <filename>]

Flags:

- `/format` - Output format as text, XML, or CSV. Valid options are `txt`, `xml`, or `csv`.

- `/output-file` - Output file.

## /associate

Associates or pairs an endpoint. This tool implements most supported pairing ceremonies. The ceremony options allow the tool to associate endpoints without extra user input.

Set Pairing

Not all protocols are set-pairing aware.

This tool will chain set associations sequentially as an implementation detail; although, most protocols don't impose this limitation.

Some protocols require set member IDs to be provided up front using the `/set [<id2>[,<id3>[,...]]]]` option.

Other protocols, like Bluetooth, can only discover other set IDs after the primary endpoint's association is finalized. These other discovered set endpoints will be associated sequentially.

Per-user Pairing

Not all protocols are per-user association aware.

For protocols that do, they generally only create PnP state visible to the user performing the pairing.

```syntax
  /associate <id1> [/set [<id2>[,<id3>[,...]]]] [/per-user [<sid>]]
                   [/protection <none | encryption | authentication>] 
                   [/just-works] [/pin-display] [/pin-entry pin] [/pin-match] 
```

Flags:

- `/set` - Associate endpoints as a set with optional secondary endpoint IDs.

- `/per-user` - Associate endpoint just for current user, or user of provided SID.

- `/protection` - Protection level for pairing connection.

- `/just-works` - Use just-works, push-button, or similar ceremony.

- `/pin-display` - Use pin-display or similar ceremony that displays pin data from the device.

- `/pin-entry` - Use pin-entry or similar ceremony.

- `/pin-match` - Use pin-match or similar ceremony.

## /associate-oob

Associates or in other words pairs an endpoint using a binary out-of-band (OOB) blob. This tool implements most supported pairing ceremonies. The ceremony options allow the tool to associate endpoints without extra user input.

```syntax
  /associate-oob <protocol> </blob <...>> | </file <...>>
                 [/just-works] [/pin-display] [/pin-entry pin] [/pin-match] 
```

Flags:

- `/blob` - Blob data as a string.

- `/file` - File containing blob data.

- `/just-works` - Use just-works, push-button, etc. ceremony.

- `/pin-display` - Use pin-display or similar ceremony that displays pin data from the device.

- `/pin-entry` - Use pin-entry or similar ceremony.

- `/pin-match` - Use pin-match or similar ceremony.

## /disassociate

Disassociates or unpairs an endpoint.

```syntax
/disassociate <id>
```

## /challenge

Challenge the OS to verify if an associated endpoint is currently present.

```syntax
/challenge <id>
```

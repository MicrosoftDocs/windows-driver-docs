---
title: PairTool Command Syntax
description: How to run PairTool, including syntax and parameters.
ms.date: 11/08/2023
---

# PairTool command syntax

> [!IMPORTANT]
> PairTool is currently in PREVIEW.
> This information relates to a prerelease product that may be substantially modified before it's released. Microsoft makes no warranties, expressed or implied, with respect to the information provided here.

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

- `/protocol` - Protocol(s) with which to discover. Use commas to separate multiple protocols. Possible protocols are enumerated with the [`/enum-protocols`](#enum-protocols) command. Protocol ID and class values are acceptable inputs.

- `/persisted` - Enumerate endpoints persisted in the OS. The `/persisted` option doesn't initiate over-the-wire discovery.

- `/sync` - Hold results until fully enumerated. The `/sync` flag can take a long time to return any results. Many protocols don't support the concept of fully enumerated, so these protocols use long timeouts instead.

- `/instance` - Endpoint instance(s) to discover directly. Use commas to separate multiple instance ID values. The `instance` flag allows for what some protocols describe as directed discovery.

- `/continuous` - Continue enumerating until Ctrl+C is pressed.

- `/url` - Update PNPX remote address for directed discovery.

- `/format` - Output format. Valid options are `txt`, `xml`, or `csv`.

- `/output-file` - Output file.

## /enum-services

Enumerates device endpoint services over the various protocols Windows supports. An endpoint service is a programmatic contract for functionality the endpoint supports. Examples of endpoint services: Bluetooth GATT, UPnP Digital Media Renderer (DMR), or ESCL scanning.

```syntax
  /enum-services [/protocol <protocol1>[,<protocol2>[,...]] [/persisted] [/sync]
                 [/instance <id1>[,<id2>[,...]] [/continuous] 
                 [/format <txt | xml | csv>] [/output-file <filename>] 
```

Flags:

- `/protocol` - Protocol(s) to discover with. Use commas to separate multiple protocol values.

- `/sync` - Hold results until fully enumerated. The `/sync` flag can take a long time to return any results. Many protocols don't support the fully enumerated concept, so these protocols use long timeouts instead.

- `/instance` - Directed discovery of a specific service instance(s). Use commas to separate multiple instance ID values.

- `/continuous` - Continue enumerating until Ctrl+C is pressed.

- `/format` - Output format as text, XML, or CSV. Valid options are `txt`, `xml`, or `csv`.

- `/output-file` - Output file.

## /enum-containers

Enumerates device endpoint containers over the various protocols Windows supports. An endpoint container is a collection of one or more endpoints over one or more protocols that conceptually represent what an end-user might perceive as the actual physical device. Examples of endpoint containers: an XBOX on your network, an NAS, or a smart TV.

```syntax
  /enum-containers [/protocol <protocol1>[,<protocol2>[,...]] [/persisted]
                   [/sync] [/instance <id1>[,<id2>[,...]] [/continuous] 
                   [/format <txt | xml | csv>] [/output-file <filename>] 
```

Flags:

- `/protocol` - Protocol(s) to discover with. Use commas to separate multiple protocol values.

- `/sync` - Hold results until fully enumerated. The `/sync` flag can take a long time to return any results. Many protocols don't support the fully enumerated concept, so these protocols use long timeouts are used instead.

- `/instance` - Directed discovery of specific container instances.

- `/continuous` - Continue enumerating until Ctrl+C is pressed.

- `/format` - Output format as text, XML, or CSV. Valid options are `txt`, `xml`, or `csv`.

- `/output-file` - Output file.

## /enum-protocols

Enumerates protocols supported in the OS this tool is running on.

```syntax
/enum-protocols [/format <txt | xml | csv>] [/output-file <filename>]
```

Flags:

- `/format` - Output format as text, XML, or CSV. Valid options are `txt`, `xml`, or `csv`.

- `/output-file` - Output file.

## /associate

Associates or pairs an endpoint. This tool implements most supported pairing ceremonies. The ceremony options allow the tool to associate endpoints without extra user input.

### Set Pairing

Not all protocols are set-pairing aware.

This tool chain sets associations sequentially as an implementation detail. Although most protocols don't impose this limitation.

Some protocols require set member IDs to be provided up front using the `/set [<id2>[,<id3>[,...]]]]` option.

Other protocols, like Bluetooth, can only discover other set IDs after the primary endpoint's association is finalized. These other discovered set endpoints are associated sequentially.

### Per-user Pairing

Not all protocols are per-user association aware. For protocols that do, they only create PnP state visible to the user performing the pairing.

```syntax
  /associate <id1> [/set [<id2>[,<id3>[,...]]]] [/per-user [<sid>]]
                   [/protection <none | encryption | authentication>] 
                   [/just-works] [/pin-display] [/pin-entry pin] [/pin-match] 
```

Flags:

- `/set` - Associate endpoints as a set with optional, comma separated, secondary endpoint IDs.

- `/per-user` - Associate endpoint just for current user, or user of provided SID.

- `/protection` - Protection level for pairing connection. Valid options are `none`, `encryption`, and `authentication`. If this option is omitted, the protocol uses the default protection level, which is typically the highest level supported by the device.

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

## Related articles

- [PairTool](pairtool.md)
- [PairTool examples](pairtool-examples.md)

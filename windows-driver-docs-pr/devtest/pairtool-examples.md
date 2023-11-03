---
title: PairTool examples
description: This article shows examples of how to use the PairTool utility.
ms.date: 11/03/2023
prerelease: true
---

# PairTool examples

This article shows examples of how to use the PairTool utility.

> [!IMPORTANT]
> PairTool is currently in PREVIEW.
> This information relates to a prerelease product that may be substantially modified before it's released. Microsoft makes no warranties, expressed or implied, with respect to the information provided here.

## /enum-protocols

Discover what protocols are installed and supported on this version on Windows. Enumerating protocols can be useful to scope down endpoint discovery over specific protocols instead of all protocols. Aside from reducing many extra results, it can also be useful for performance. Discovery, particularly over wireless protocols, can be expensive in terms of power consumption and QoS, so should be avoided when not needed. Protocols like Bluetooth and WiFiDirect sometimes share the same radio hardware, which degrades the QoS of discovery when running at the same time. When QoS degrades, devices can't be discovered reliably. It's typically better not to use them both at the same time.

```cmd
pairtool /enum-protocols
```

## /enum-endpoints

Discover devices over all protocols.

```cmd
pairtool /enum-endpoints
```

Discover only Bluetooth devices.

```cmd
pairtool /enum-endpoints /protocol Bluetooth,BluetoothLE
```

Discover what devices are paired without active on-the-wire discovery over the protocol. Since enumerating endpoints doesn't activate discovery over the protocol, this discover method has the lowest cost.

```cmd
pairtool /enum-endpoints /persisted
```

Save all discoverable Bluetooth devices to an XML file without updates.

```cmd
pairtool /enum-endpoints /protocol Bluetooth,BluetoothLE /sync /format XML /output-file out.xml
```

## /associate

Associate an endpoint. For associate to work, typically and endpoint would have `Associable: true` when enumerated. If no other parameters are passed, then pairing ceremonies that require input collect the input, like a PIN, from the console.

```cmd
pairtool /associate BluetoothLE#BluetoothLEdc:46:28:6a:16:01-d8:02:ba:2b:9e:2c
```

Automatically associate an endpoint without input, using just-works or similar ceremony. If the device supports one of these ceremonies, the device is selected, and pairing completes without user interaction.

```cmd
pairtool /associate BluetoothLE#BluetoothLEdc:46:28:6a:16:01-d8:02:ba:2b:9e:2c /just-works
```

Associate more an endpoint as a set. For Bluetooth- style set pairing, the other endpoints of the set are  discovered at the end of the pairing ceremony. This tool automatically starts pairing the other set members in sequence.

```cmd
pairtool /associate BluetoothLE#BluetoothLEdc:46:28:6a:16:01-d8:02:ba:2b:9e:2c /set
```

Associate more than one endpoint as a set. This method also synchronizes device creation, as needed. Supplied set members are paired sequentially. If more set members are discovered as a result of pairing the specified endpoints, they're also paired sequentially.

```cmd
pairtool /associate DAFWSDProvider#urn:uuid:7efbca06-1e97-4ada-b85a-9c6ca59497fc /set IPP#7efbca06-1e97-4ada-b85a-9c6ca59497fc
```

Associate an endpoint just for the current user.

```cmd
pairtool /associate MCP#ab589c5e-d5c0-430f-a3f0-7295b421021a /per-user
```

Associate an endpoint just for a specific user SID.

```cmd
pairtool /associate MCP#ab589c5e-d5c0-430f-a3f0-7295b421021a /per-user S-1-12-1-5555
```

## /disassociate

Unpair an endpoint.

```cmd
pairtool /disassociate BluetoothLE#BluetoothLEdc:46:28:6a:16:01-d8:02:ba:2b:9e:2c
```

## /challenge

Challenge the liveness of the PnP device state of a paired endpoint. This challenge is useful if an endpoint's device state appears to be incorrectly online or offline.

```cmd
pairtool /challenge MCP#8317e7db-8bac-40ca-bfa5-467735c06866
```

## Related articles

- [PairTool](pairtool.md)
- [PairTool command syntax](pairtool-command-syntax.md)

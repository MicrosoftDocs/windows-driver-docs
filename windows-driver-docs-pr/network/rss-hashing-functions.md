---
title: RSS Hashing Functions
description: RSS Hashing Functions
ms.assetid: e7698573-c3d1-4ac6-a985-93cf7fc6e585
keywords:
- receive-side scaling WDK networking , hash
- RSS WDK networking , hash
- hash WDK RSS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# RSS Hashing Functions


## Overview

A NIC or its miniport driver uses the RSS hashing function to calculate an RSS hash value.

Overlying drivers set the hash type, function, and table to assign connections to CPUs. For more information, see [RSS Configuration](rss-configuration.md).

The hashing function can be one of the following:

- **NdisHashFunctionToeplitz**
- **NdisHashFunctionReserved1**
- **NdisHashFunctionReserved2**
- **NdisHashFunctionReserved3**

>[!NOTE]
> Currently, **NdisHashFunctionToeplitz** is the only hashing function available to miniport drivers. The other hashing functions are reserved for NDIS. 

A miniport driver should identify the hashing function and value that it uses in each [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure before the driver indicates received data. For more information, see [Indicating RSS Receive Data](indicating-rss-receive-data.md).

## Examples

The following four pseudocode examples show how to calculate the **NdisHashFunctionToeplitz** hash value. These examples represent the four possible hash types that are available for **NdisHashFunctionToeplitz**. For more information about hash types, see [RSS Hashing Types](rss-hashing-types.md).

To simplify the examples, a generalized algorithm that processes an input byte stream is required. Specific formats for the byte streams are defined later in the four examples.

The overlying driver provides a secret key (K) to the miniport driver for use in the hash calculation. The key is 40 bytes (320 bits) long. For more information about the key, see [RSS Configuration](rss-configuration.md).

Given an input array that contains *n* bytes, the byte stream is defined as follows:

```c++
input[0] input[1] input[2] ... input[n-1]
```

The left-most byte is input\[0\], and the most-significant bit of input\[0\] is the left-most bit. The right-most byte is input\[n-1\], and the least-significant bit of input\[n-1\] is the right-most bit.

Given the preceding definitions, the pseudocode for processing a general input byte stream is defined as follows:

```c++
ComputeHash(input[], n)

result = 0
For each bit b in input[] from left to right
{
if (b == 1) result ^= (left-most 32 bits of K)
shift K left 1 bit position
}

return result
```

The pseudocode contains entries of the form @n-m. These entries identify the byte range of each element in the TCP packet.

### Example Hash Calculation for IPv4 with the TCP Header

Concatenate the SourceAddress, DestinationAddress, SourcePort, and DestinationPort fields of the packet into a byte array, preserving the order in which they occurred in the packet:

```c++
Input[12] = @12-15, @16-19, @20-21, @22-23
Result = ComputeHash(Input, 12)
```

### Example Hash Calculation for IPv4 Only

Concatenate the SourceAddress and DestinationAddress fields of the packet into a byte array.

```c++
Input[8] = @12-15, @16-19
Result = ComputeHash(Input, 8) 
```

### Example Hash Calculation for IPv6 with the TCP Header

Concatenate the SourceAddress, DestinationAddress, SourcePort, and DestinationPort fields of the packet into a byte array, preserving the order in which they occurred in the packet.

```c++
Input[36] = @8-23, @24-39, @40-41, @42-43
Result = ComputeHash(Input, 36)
```

### Example Hash Calculation for IPv6 Only

Concatenate the SourceAddress and DestinationAddress fields of the packet into a byte array.

```c++
Input[32] = @8-23, @24-39
Result = ComputeHash(Input, 32)
```

 

 






---
title: Debugging NetAdapterCx Client Drivers
---

# Debugging NetAdapterCx Client Drivers

You can use [Windows Driver Framework Extensions (Wdfkd.dll)](https://msdn.microsoft.com/library/windows/hardware/ff551876) commands to debug your client driver.  In addition, you can provide a NETADAPTER handle to [`!ndiskd.netadapter`](https://msdn.microsoft.com/en-us/library/windows/hardware/mt799821(v=vs.85).aspx) to see networking-specific properties of your driver.

Also, you can use the `!ndiskd.netrb` debugger extension with the address of a [**NET_RING_BUFFER**](net-ring-buffer.md) structure to examine packets and fragments in a ring buffer.  This command gives you additional information, such as the number of elements in the ring buffer, along with the number of packets owned by the OS and the number of packets owned by the client.

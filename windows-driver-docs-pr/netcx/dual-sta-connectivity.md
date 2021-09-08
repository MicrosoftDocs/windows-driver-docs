9	DUAL STA CONNECTIVITY

WiFiCx enables simultaneous connections to more than one STA (secondary sta connectivity) when the driver supports it. In its initial iteration, it only supports a maximum of two STA connections, but that can change later.

9.1	CAPABILITY

The driver indicates the ability to maintain Secondary STA connectivity in the call to [**WifiDeviceSetStationCapabilities**](/windows-hardware/drivers/ddi/wificx/nf-wificx-wifidevicesetstationcapabilities). The driver must set the **NumSecondaryStaBandCombinations** and **SecondaryStaBandsCombinations** fields to non-zero values in the [**WIFI_STATION_CAPABILITIES**](/windows-hardware/drivers/ddi/wificx/ns-wificx-wifi_station_capabilities) structure. If either of those values are 0/NULL, then Secondary STA capability will not be set.

9.2	CURRENT BEHAVIOR

When the adapter supports Secondary STA connectivity, there should be no full scan on the Secondary STA since the Secondary STA is not visible to the user. The exception is for specific-purpose scans such as when connecting over the Secondary STA to discover connection candidates, or possibly for Neighbor reports. If the driver sees a scan request over the Secondary STA, it should avoid scanning over the Primary STA to minimize disruptions. The exception might be for co-located APs in the 6 GHz – only if they cannot be discovered on the other lower band scan.
When secondary sta connectivity is supported by the driver, connections over the Secondary STA are automatically synchronized with the Primary STA. The initial connection over the Secondary STA will start immediately after the Primary STA connection succeeds, and will then follow a backoff timeout in case of failure.

9.3	WIFICX API TLV CHANGES

Most of the API changes for enabling Secondary STA connectivity are documented in the following sections:
2.3.2 (TLV Types)
3.3.2 (WDI_CONNECT_PARAMETERS)
5.19 (WDI_INDICATION_SECONDARY_STA_CONNECTIVITY)
5.2 (WDI_INDICATION_LINK_STATE_CHANGE)
9.4	SECONDARY STA ROAM BEHAVIOR

The driver should make a best-effort to keep the secondary sta up while roaming on the primary sta band – even if it has to roam across bands. It should do this by synchronizing the roams so that both interfaces don’t end up roaming at the sam time. The driver should keep the secondary sta up, and wait for the roam to finish on the primary sta port (upto the point where the keys are plumbed for a secure connection) so that it can then select the appropriate roaming candidates for the secondary sta connection (on a different band than the primary sta):
This will enable apps that are bound to both the primary and secondary sta interfaces to keep their connections up during the roam.

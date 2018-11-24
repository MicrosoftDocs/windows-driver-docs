---
title: NDIS Interface Types
description: This topic describes types for NDIS Interfaces.
ms.assetid: 80320da2-d35f-41de-b001-2cb71d202ccc
keywords:
- NDIS Interface Types, WDK NDIS Interface Types network drivers
ms.date: 11/27/2017
ms.localizationpriority: medium
---

# NDIS Interface Types

NDIS interface types correspond to the *IfType* object that is defined in the management information base (MIB). These interface types are used in the **IfType** members and *IfType* parameters for many NDIS structures and functions.

NDIS interface types are registered with the Internet Assigned Numbers Authority (IANA), which publishes a list of interface types periodically in the Assigned Numbers RFC, or in a derivative of it that is specific to Internet network management number assignments. For more information about the IANA IfType *definitions*, see [IANA ifType MIB Definitions](http://go.microsoft.com/fwlink/p/?linkid=60066). For more information about the IANA, see the [IANA](http://go.microsoft.com/fwlink/p/?linkid=60068) Web site.

The following table describes IfType values.

<table>
<tr><th>Name</th><th>Value</th><th>Comment</th></tr>
<tr><td data-th="Name">
<p>IF_TYPE_OTHER</p>
</td><td data-th="Value">
<p>1</p>
</td><td data-th="Comment">
<p>Use this value if none of the other IF_TYPE_<em>Xxx</em> types applies.</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_REGULAR_1822</p>
</td><td data-th="Value">
<p>2</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_HDH_1822</p>
</td><td data-th="Value">
<p>3</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_DDN_X25</p>
</td><td data-th="Value">
<p>4</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_RFC877_X25</p>
</td><td data-th="Value">
<p>5</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ETHERNET_CSMACD</p>
</td><td data-th="Value">
<p>6</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_IS088023_CSMACD</p>
</td><td data-th="Value">
<p>7</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ISO88024_TOKENBUS</p>
</td><td data-th="Value">
<p>8</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ISO88025_TOKENRING</p>
</td><td data-th="Value">
<p>9</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ISO88026_MAN</p>
</td><td data-th="Value">
<p>10</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_STARLAN</p>
</td><td data-th="Value">
<p>11</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_PROTEON_10MBIT</p>
</td><td data-th="Value">
<p>12</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_PROTEON_80MBIT</p>
</td><td data-th="Value">
<p>13</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_HYPERCHANNEL</p>
</td><td data-th="Value">
<p>14</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_FDDI</p>
</td><td data-th="Value">
<p>15</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_LAP_B</p>
</td><td data-th="Value">
<p>16</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_SDLC</p>
</td><td data-th="Value">
<p>17</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_DS1</p>
</td><td data-th="Value">
<p>18</p>
</td><td data-th="Comment">
<p>DS1-MIB</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_E1</p>
</td><td data-th="Value">
<p>19</p>
</td><td data-th="Comment">
<p>Obsolete. See DS1-MIB.</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_BASIC_ISDN</p>
</td><td data-th="Value">
<p>20</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_PRIMARY_ISDN</p>
</td><td data-th="Value">
<p>21</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_PROP_POINT2POINT_SERIAL</p>
</td><td data-th="Value">
<p>22</p>
</td><td data-th="Comment">
<p>Proprietary serial</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_PPP</p>
</td><td data-th="Value">
<p>23</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_SOFTWARE_LOOPBACK</p>
</td><td data-th="Value">
<p>24</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_EON</p>
</td><td data-th="Value">
<p>25</p>
</td><td data-th="Comment">
<p>CLNP over IP</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ETHERNET_3MBIT</p>
</td><td data-th="Value">
<p>26</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_NSIP</p>
</td><td data-th="Value">
<p>27</p>
</td><td data-th="Comment">
<p>XNS over IP</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_SLIP</p>
</td><td data-th="Value">
<p>28</p>
</td><td data-th="Comment">
<p>Generic Slip</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ULTRA</p>
</td><td data-th="Value">
<p>29</p>
</td><td data-th="Comment">
<p>ULTRA Technologies</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_DS3</p>
</td><td data-th="Value">
<p>30</p>
</td><td data-th="Comment">
<p>DS3-MIB</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_SIP</p>
</td><td data-th="Value">
<p>31</p>
</td><td data-th="Comment">
<p>SMDS and coffee</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_FRAMERELAY</p>
</td><td data-th="Value">
<p>32</p>
</td><td data-th="Comment">
<p>DTE only</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_RS232</p>
</td><td data-th="Value">
<p>33</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_PARA</p>
</td><td data-th="Value">
<p>34</p>
</td><td data-th="Comment">
<p>Parallel port</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ARCNET</p>
</td><td data-th="Value">
<p>35</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ARCNET_PLUS</p>
</td><td data-th="Value">
<p>36</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ATM</p>
</td><td data-th="Value">
<p>37</p>
</td><td data-th="Comment">
<p>ATM cells</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_MIO_X25</p>
</td><td data-th="Value">
<p>38</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_SONET</p>
</td><td data-th="Value">
<p>39</p>
</td><td data-th="Comment">
<p>SONET or SDH</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_X25_PLE</p>
</td><td data-th="Value">
<p>40</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ISO88022_LLC</p>
</td><td data-th="Value">
<p>41</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_LOCALTALK</p>
</td><td data-th="Value">
<p>42</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_SMDS_DXI</p>
</td><td data-th="Value">
<p>43</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_FRAMERELAY_SERVICE</p>
</td><td data-th="Value">
<p>44</p>
</td><td data-th="Comment">
<p>FRNETSERV-MIB</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_V35</p>
</td><td data-th="Value">
<p>45</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_HSSI</p>
</td><td data-th="Value">
<p>46</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_HIPPI</p>
</td><td data-th="Value">
<p>47</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_MODEM</p>
</td><td data-th="Value">
<p>48</p>
</td><td data-th="Comment">
<p>Generic modem</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_AAL5</p>
</td><td data-th="Value">
<p>49</p>
</td><td data-th="Comment">
<p>AAL5 over ATM</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_SONET_PATH</p>
</td><td data-th="Value">
<p>50</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_SONET_VT</p>
</td><td data-th="Value">
<p>51</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_SMDS_ICIP</p>
</td><td data-th="Value">
<p>52</p>
</td><td data-th="Comment">
<p>SMDS InterCarrier interface</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_PROP_VIRTUAL</p>
</td><td data-th="Value">
<p>53</p>
</td><td data-th="Comment">
<p>Proprietary virtual/internal</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_PROP_MULTIPLEXOR</p>
</td><td data-th="Value">
<p>54</p>
</td><td data-th="Comment">
<p>Proprietary multiplexing</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_IEEE80212</p>
</td><td data-th="Value">
<p>55</p>
</td><td data-th="Comment">
<p>100BaseVG</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_FIBRECHANNEL</p>
</td><td data-th="Value">
<p>56</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_HIPPIINTERFACE</p>
</td><td data-th="Value">
<p>57</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_FRAMERELAY_INTERCONNECT</p>
</td><td data-th="Value">
<p>58</p>
</td><td data-th="Comment">
<p>Obsolete. Use 32 or 44 instead.</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_AFLANE_8023</p>
</td><td data-th="Value">
<p>59</p>
</td><td data-th="Comment">
<p>ATM-emulated LAN-for 802.3</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_AFLANE_8025</p>
</td><td data-th="Value">
<p>60</p>
</td><td data-th="Comment">
<p>ATM-emulated LAN for 802.5</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_CCTEMUL</p>
</td><td data-th="Value">
<p>61</p>
</td><td data-th="Comment">
<p>ATM-emulated circuit</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_FASTETHER</p>
</td><td data-th="Value">
<p>62</p>
</td><td data-th="Comment">
<p>Fast Ethernet (100BaseT)</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ISDN</p>
</td><td data-th="Value">
<p>63</p>
</td><td data-th="Comment">
<p>ISDN and X.25</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_V11</p>
</td><td data-th="Value">
<p>64</p>
</td><td data-th="Comment">
<p>CCITT V.11/X.21</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_V36</p>
</td><td data-th="Value">
<p>65</p>
</td><td data-th="Comment">
<p>CCITT V.36</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_G703_64K</p>
</td><td data-th="Value">
<p>66</p>
</td><td data-th="Comment">
<p>CCITT G703 at 64Kbps</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_G703_2MB</p>
</td><td data-th="Value">
<p>67</p>
</td><td data-th="Comment">
<p>Obsolete. See DS1-MIB.</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_QLLC</p>
</td><td data-th="Value">
<p>68</p>
</td><td data-th="Comment">
<p>SNA QLLC</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_FASTETHER_FX</p>
</td><td data-th="Value">
<p>69</p>
</td><td data-th="Comment">
<p>Fast Ethernet (100BaseFX)</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_CHANNEL</p>
</td><td data-th="Value">
<p>70</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_IEEE80211</p>
</td><td data-th="Value">
<p>71</p>
</td><td data-th="Comment">
<p>Radio spread spectrum</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_IBM370PARCHAN</p>
</td><td data-th="Value">
<p>72</p>
</td><td data-th="Comment">
<p>IBM System 360/370 OEMI channel</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ESCON</p>
</td><td data-th="Value">
<p>73</p>
</td><td data-th="Comment">
<p>IBM Enterprise Systems connection</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_DLSW</p>
</td><td data-th="Value">
<p>74</p>
</td><td data-th="Comment">
<p>Data link switching</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ISDN_S</p>
</td><td data-th="Value">
<p>75</p>
</td><td data-th="Comment">
<p>ISDN S/T interface</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ISDN_U</p>
</td><td data-th="Value">
<p>76</p>
</td><td data-th="Comment">
<p>ISDN U interface</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_LAP_D</p>
</td><td data-th="Value">
<p>77</p>
</td><td data-th="Comment">
<p>Link access protocol D</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_IPSWITCH</p>
</td><td data-th="Value">
<p>78</p>
</td><td data-th="Comment">
<p>IP switching objects</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_RSRB</p>
</td><td data-th="Value">
<p>79</p>
</td><td data-th="Comment">
<p>Remote source route bridging</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ATM_LOGICAL</p>
</td><td data-th="Value">
<p>80</p>
</td><td data-th="Comment">
<p>ATM logical port</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_DS0</p>
</td><td data-th="Value">
<p>81</p>
</td><td data-th="Comment">
<p>Digital signal level 0</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_DS0_BUNDLE</p>
</td><td data-th="Value">
<p>82</p>
</td><td data-th="Comment">
<p>Group of ds0s on the same ds1</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_BSC</p>
</td><td data-th="Value">
<p>83</p>
</td><td data-th="Comment">
<p>Bisynchronous protocol</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ASYNC</p>
</td><td data-th="Value">
<p>84</p>
</td><td data-th="Comment">
<p>Asynchronous protocol</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_CNR</p>
</td><td data-th="Value">
<p>85</p>
</td><td data-th="Comment">
<p>Combat net radio</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ISO88025R_DTR</p>
</td><td data-th="Value">
<p>86</p>
</td><td data-th="Comment">
<p>ISO 802.5r DTR</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_EPLRS</p>
</td><td data-th="Value">
<p>87</p>
</td><td data-th="Comment">
<p>Ext Pos Loc Report Sys</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ARAP</p>
</td><td data-th="Value">
<p>88</p>
</td><td data-th="Comment">
<p>Appletalk remote access protocol</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_PROP_CNLS</p>
</td><td data-th="Value">
<p>89</p>
</td><td data-th="Comment">
<p>Proprietary connectionless protocol</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_HOSTPAD</p>
</td><td data-th="Value">
<p>90</p>
</td><td data-th="Comment">
<p>CCITT-ITU X.29 PAD protocol</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_TERMPAD</p>
</td><td data-th="Value">
<p>91</p>
</td><td data-th="Comment">
<p>CCITT-ITU X.3 PAD facility</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_FRAMERELAY_MPI</p>
</td><td data-th="Value">
<p>92</p>
</td><td data-th="Comment">
<p>Multiproto interconnect over FR</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_X213</p>
</td><td data-th="Value">
<p>93</p>
</td><td data-th="Comment">
<p>CCITT-ITU X213</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ADSL</p>
</td><td data-th="Value">
<p>94</p>
</td><td data-th="Comment">
<p>Asymmetric digital subscriber loop</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_RADSL</p>
</td><td data-th="Value">
<p>95</p>
</td><td data-th="Comment">
<p>Rate-adapt digital subscriber loop</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_SDSL</p>
</td><td data-th="Value">
<p>96</p>
</td><td data-th="Comment">
<p>Symmetric digital subscriber loop</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_VDSL</p>
</td><td data-th="Value">
<p>97</p>
</td><td data-th="Comment">
<p>Very H-Speed digital subscriber loop</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ISO88025_CRFPRINT</p>
</td><td data-th="Value">
<p>98</p>
</td><td data-th="Comment">
<p>ISO 802.5 CRFP</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_MYRINET</p>
</td><td data-th="Value">
<p>99</p>
</td><td data-th="Comment">
<p>Myricom Myrinet</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_VOICE_EM</p>
</td><td data-th="Value">
<p>100</p>
</td><td data-th="Comment">
<p>Voice recEive and transMit</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_VOICE_FXO</p>
</td><td data-th="Value">
<p>101</p>
</td><td data-th="Comment">
<p>Voice foreign exchange office</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_VOICE_FXS</p>
</td><td data-th="Value">
<p>102</p>
</td><td data-th="Comment">
<p>Voice foreign exchange station</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_VOICE_ENCAP</p>
</td><td data-th="Value">
<p>103</p>
</td><td data-th="Comment">
<p>Voice encapsulation</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_VOICE_OVERIP</p>
</td><td data-th="Value">
<p>104</p>
</td><td data-th="Comment">
<p>Voice over IP encapsulation</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ATM_DXI</p>
</td><td data-th="Value">
<p>105</p>
</td><td data-th="Comment">
<p>ATM DXI</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ATM_FUNI</p>
</td><td data-th="Value">
<p>106</p>
</td><td data-th="Comment">
<p>ATM FUNI</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ATM_IMA</p>
</td><td data-th="Value">
<p>107</p>
</td><td data-th="Comment">
<p>ATM IMA</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_PPPMULTILINKBUNDLE</p>
</td><td data-th="Value">
<p>108</p>
</td><td data-th="Comment">
<p>PPP multilink bundle</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_IPOVER_CDLC</p>
</td><td data-th="Value">
<p>109</p>
</td><td data-th="Comment">
<p>IBM ipOverCdlc</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_IPOVER_CLAW</p>
</td><td data-th="Value">
<p>110</p>
</td><td data-th="Comment">
<p>IBM common link access to workstation</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_STACKTOSTACK</p>
</td><td data-th="Value">
<p>111</p>
</td><td data-th="Comment">
<p>IBM stackToStack</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_VIRTUALIPADDRESS</p>
</td><td data-th="Value">
<p>112</p>
</td><td data-th="Comment">
<p>IBM VIPA</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_MPC</p>
</td><td data-th="Value">
<p>113</p>
</td><td data-th="Comment">
<p>IBM multi-proto channel support</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_IPOVER_ATM</p>
</td><td data-th="Value">
<p>114</p>
</td><td data-th="Comment">
<p>IBM ipOverAtm</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ISO88025_FIBER</p>
</td><td data-th="Value">
<p>115</p>
</td><td data-th="Comment">
<p>ISO 802.5j Fiber Token Ring</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_TDLC</p>
</td><td data-th="Value">
<p>116</p>
</td><td data-th="Comment">
<p>IBM twinaxial data link control</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_GIGABITETHERNET</p>
</td><td data-th="Value">
<p>117</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_HDLC</p>
</td><td data-th="Value">
<p>118</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_LAP_F</p>
</td><td data-th="Value">
<p>119</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_V37</p>
</td><td data-th="Value">
<p>120</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_X25_MLP</p>
</td><td data-th="Value">
<p>121</p>
</td><td data-th="Comment">
<p>Multi-link protocol</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_X25_HUNTGROUP</p>
</td><td data-th="Value">
<p>122</p>
</td><td data-th="Comment">
<p>X.25 hunt group</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_TRANSPHDLC</p>
</td><td data-th="Value">
<p>123</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_INTERLEAVE</p>
</td><td data-th="Value">
<p>124</p>
</td><td data-th="Comment">
<p>Interleave channel</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_FAST</p>
</td><td data-th="Value">
<p>125</p>
</td><td data-th="Comment">
<p>Fast channel</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_IP</p>
</td><td data-th="Value">
<p>126</p>
</td><td data-th="Comment">
<p>IP (for APPN HPR in IP networks)</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_DOCSCABLE_MACLAYER</p>
</td><td data-th="Value">
<p>127</p>
</td><td data-th="Comment">
<p>CATV MAC layer</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_DOCSCABLE_DOWNSTREAM</p>
</td><td data-th="Value">
<p>128</p>
</td><td data-th="Comment">
<p>CATV downstream interface</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_DOCSCABLE_UPSTREAM</p>
</td><td data-th="Value">
<p>129</p>
</td><td data-th="Comment">
<p>CATV upstream interface</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_A12MPPSWITCH</p>
</td><td data-th="Value">
<p>130</p>
</td><td data-th="Comment">
<p>Avalon parallel processor</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_TUNNEL</p>
</td><td data-th="Value">
<p>131</p>
</td><td data-th="Comment">
<p>Encapsulation interface</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_COFFEE</p>
</td><td data-th="Value">
<p>132</p>
</td><td data-th="Comment">
<p>Coffee pot</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_CES</p>
</td><td data-th="Value">
<p>133</p>
</td><td data-th="Comment">
<p>Circuit emulation service</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ATM_SUBINTERFACE</p>
</td><td data-th="Value">
<p>134</p>
</td><td data-th="Comment">
<p>ATM sub-interface</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_L2_VLAN</p>
</td><td data-th="Value">
<p>135</p>
</td><td data-th="Comment">
<p>Layer 2 virtual LAN using 802.1Q</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_L3_IPVLAN</p>
</td><td data-th="Value">
<p>136</p>
</td><td data-th="Comment">
<p>Layer 3 virtual LAN using IP</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_L3_IPXVLAN</p>
</td><td data-th="Value">
<p>137</p>
</td><td data-th="Comment">
<p>Layer 3 virtual LAN using IPX</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_DIGITALPOWERLINE</p>
</td><td data-th="Value">
<p>138</p>
</td><td data-th="Comment">
<p>IP over power lines</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_MEDIAMAILOVERIP</p>
</td><td data-th="Value">
<p>139</p>
</td><td data-th="Comment">
<p>Multimedia mail over IP</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_DTM</p>
</td><td data-th="Value">
<p>140</p>
</td><td data-th="Comment">
<p>Dynamic synchronous transfer mode</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_DCN</p>
</td><td data-th="Value">
<p>141</p>
</td><td data-th="Comment">
<p>Data communications network</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_IPFORWARD</p>
</td><td data-th="Value">
<p>142</p>
</td><td data-th="Comment">
<p>IP forwarding interface</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_MSDSL</p>
</td><td data-th="Value">
<p>143</p>
</td><td data-th="Comment">
<p>Multi-rate symmetric DSL</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_IEEE1394</p>
</td><td data-th="Value">
<p>144</p>
</td><td data-th="Comment">
<p>IEEE 1394 high performance serial bus</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_IF_GSN</p>
</td><td data-th="Value">
<p>145</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_DVBRCC_MACLAYER</p>
</td><td data-th="Value">
<p>146</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_DVBRCC_DOWNSTREAM</p>
</td><td data-th="Value">
<p>147</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_DVBRCC_UPSTREAM</p>
</td><td data-th="Value">
<p>148</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ATM_VIRTUAL</p>
</td><td data-th="Value">
<p>149</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_MPLS_TUNNEL</p>
</td><td data-th="Value">
<p>150</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_SRP</p>
</td><td data-th="Value">
<p>151</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_VOICEOVERATM</p>
</td><td data-th="Value">
<p>152</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_VOICEOVERFRAMERELAY</p>
</td><td data-th="Value">
<p>153</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_IDSL</p>
</td><td data-th="Value">
<p>154</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_COMPOSITELINK</p>
</td><td data-th="Value">
<p>155</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_SS7_SIGLINK</p>
</td><td data-th="Value">
<p>156</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_PROP_WIRELESS_P2P</p>
</td><td data-th="Value">
<p>157</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_FR_FORWARD</p>
</td><td data-th="Value">
<p>158</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_RFC1483</p>
</td><td data-th="Value">
<p>159</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_USB</p>
</td><td data-th="Value">
<p>160</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_IEEE8023AD_LAG</p>
</td><td data-th="Value">
<p>161</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_BGP_POLICY_ACCOUNTING</p>
</td><td data-th="Value">
<p>162</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_FRF16_MFR_BUNDLE</p>
</td><td data-th="Value">
<p>163</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_H323_GATEKEEPER</p>
</td><td data-th="Value">
<p>164</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_H323_PROXY</p>
</td><td data-th="Value">
<p>165</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_MPLS</p>
</td><td data-th="Value">
<p>166</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_MF_SIGLINK</p>
</td><td data-th="Value">
<p>167</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_HDSL2</p>
</td><td data-th="Value">
<p>168</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_SHDSL</p>
</td><td data-th="Value">
<p>169</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_DS1_FDL</p>
</td><td data-th="Value">
<p>170</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_POS</p>
</td><td data-th="Value">
<p>171</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_DVB_ASI_IN</p>
</td><td data-th="Value">
<p>172</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_DVB_ASI_OUT</p>
</td><td data-th="Value">
<p>173</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_PLC</p>
</td><td data-th="Value">
<p>174</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_NFAS</p>
</td><td data-th="Value">
<p>175</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_TR008</p>
</td><td data-th="Value">
<p>176</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_GR303_RDT</p>
</td><td data-th="Value">
<p>177</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_GR303_IDT</p>
</td><td data-th="Value">
<p>178</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ISUP</p>
</td><td data-th="Value">
<p>179</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_PROP_DOCS_WIRELESS_MACLAYER</p>
</td><td data-th="Value">
<p>180</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_PROP_DOCS_WIRELESS_DOWNSTREAM</p>
</td><td data-th="Value">
<p>181</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_PROP_DOCS_WIRELESS_UPSTREAM</p>
</td><td data-th="Value">
<p>182</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_HIPERLAN2</p>
</td><td data-th="Value">
<p>183</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_PROP_BWA_P2MP</p>
</td><td data-th="Value">
<p>184</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_SONET_OVERHEAD_CHANNEL</p>
</td><td data-th="Value">
<p>185</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_DIGITAL_WRAPPER_OVERHEAD_CHANNEL</p>
</td><td data-th="Value">
<p>186</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_AAL2</p>
</td><td data-th="Value">
<p>187</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_RADIO_MAC</p>
</td><td data-th="Value">
<p>188</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ATM_RADIO</p>
</td><td data-th="Value">
<p>189</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_IMT</p>
</td><td data-th="Value">
<p>190</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_MVL</p>
</td><td data-th="Value">
<p>191</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_REACH_DSL</p>
</td><td data-th="Value">
<p>192</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_FR_DLCI_ENDPT</p>
</td><td data-th="Value">
<p>193</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_ATM_VCI_ENDPT</p>
</td><td data-th="Value">
<p>194</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_OPTICAL_CHANNEL</p>
</td><td data-th="Value">
<p>195</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_OPTICAL_TRANSPORT</p>
</td><td data-th="Value">
<p>196</p>
</td><td data-th="Comment" /></tr>
<tr><td data-th="Name">
<p>IF_TYPE_WWANPP</p>
</td><td data-th="Value">
<p>243</p>
</td><td data-th="Comment">
<p>Mobile Broadband devices based on GSM technology</p>
</td></tr>
<tr><td data-th="Name">
<p>IF_TYPE_WWANPP2</p>
</td><td data-th="Value">
<p>244</p>
</td><td data-th="Comment">
<p>Mobile Broadband devices based on CDMA technology</p>
</td></tr>
</table>


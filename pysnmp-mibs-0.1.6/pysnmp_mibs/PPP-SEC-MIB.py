#
# PySNMP MIB module PPP-SEC-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/PPP-SEC-MIB
# Produced by pysmi-0.0.7 at Sun Feb 14 00:24:35 2016
# On host bldfarm platform Linux version 4.1.13-100.fc21.x86_64 by user goose
# Using Python version 3.5.0 (default, Jan  5 2016, 17:11:52) 
#
( ObjectIdentifier, Integer, OctetString, ) = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
( ppp, ) = mibBuilder.importSymbols("PPP-LCP-MIB", "ppp")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Bits, Integer32, iso, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, Counter32, Gauge32, MibIdentifier, IpAddress, Unsigned32, ModuleIdentity, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "iso", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "Counter32", "Gauge32", "MibIdentifier", "IpAddress", "Unsigned32", "ModuleIdentity")
( TextualConvention, DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pppSecurity = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 2))
pppSecurityProtocols = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 2, 1))
pppSecurityPapProtocol = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 2, 1, 1))
pppSecurityChapMD5Protocol = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 2, 1, 2))
pppSecurityConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 2, 2), )
if mibBuilder.loadTexts: pppSecurityConfigTable.setDescription('Table containing the configuration and\n                         preference parameters for PPP Security.')
pppSecurityConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1), ).setIndexNames((0, "PPP-SEC-MIB", "pppSecurityConfigLink"), (0, "PPP-SEC-MIB", "pppSecurityConfigPreference"))
if mibBuilder.loadTexts: pppSecurityConfigEntry.setDescription('Security configuration information for a\n                         particular PPP link.')
pppSecurityConfigLink = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0,2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppSecurityConfigLink.setDescription("The value of ifIndex that identifies the entry\n                         in the interface table that is associated with\n                         the local PPP entity's link for which this\n                         particular security algorithm shall be\n                         attempted. A value of 0 indicates the default\n                         algorithm - i.e., this entry applies to all\n                         links for which explicit entries in the table\n                         do not exist.")
pppSecurityConfigPreference = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0,2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppSecurityConfigPreference.setDescription('The relative preference of the security\n                         protocol identified by\n                         pppSecurityConfigProtocol. Security protocols\n                         with lower values of\n                         pppSecurityConfigPreference are tried before\n                         protocols with higher values of\n                         pppSecurityConfigPreference.')
pppSecurityConfigProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppSecurityConfigProtocol.setDescription('Identifies the security protocol to be\n                         attempted on the link identified by\n                         pppSecurityConfigLink at the preference level\n                         identified by pppSecurityConfigPreference. ')
pppSecurityConfigStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2,))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2),)).clone('valid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppSecurityConfigStatus.setDescription('Setting this object to the value invalid(1)\n                         has the effect of invalidating the\n                         corresponding entry in the\n                         pppSecurityConfigTable. It is an\n                         implementation-specific matter as to whether\n                         the agent removes an invalidated entry from the\n                         table.  Accordingly, management stations must\n                         be prepared to receive tabular information from\n                         agents that corresponds to entries not\n                         currently in use.  Proper interpretation of\n                         such entries requires examination of the\n                         relevant pppSecurityConfigStatus object.')
pppSecuritySecretsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 2, 3), )
if mibBuilder.loadTexts: pppSecuritySecretsTable.setDescription('Table containing the identities and secrets\n                         used by the PPP authentication protocols.  As\n                         this table contains secret information, it is\n                         expected that access to this table be limited\n                         to those SNMP Party-Pairs for which a privacy\n                         protocol is in use for all SNMP messages that\n                         the parties exchange.  This table contains both\n                         the ID and secret pair(s) that the local PPP\n                         entity will advertise to the remote entity and\n                         the pair(s) that the local entity will expect\n                         from the remote entity.  This table allows for\n                         multiple id/secret password pairs to be\n                         specified for a particular link by using the\n                         pppSecuritySecretsIdIndex object.')
pppSecuritySecretsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1), ).setIndexNames((0, "PPP-SEC-MIB", "pppSecuritySecretsLink"), (0, "PPP-SEC-MIB", "pppSecuritySecretsIdIndex"))
if mibBuilder.loadTexts: pppSecuritySecretsEntry.setDescription('Secret information.')
pppSecuritySecretsLink = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0,2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppSecuritySecretsLink.setDescription('The link to which this ID/Secret pair applies.\n                         By convention, if the value of this object is 0\n                         then the ID/Secret pair applies to all links.')
pppSecuritySecretsIdIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0,2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppSecuritySecretsIdIndex.setDescription('A unique value for each ID/Secret pair that\n                         has been defined for use on this link.  This\n                         allows multiple ID/Secret pairs to be defined\n                         for each link.  How the local entity selects\n                         which pair to use is a local implementation\n                         decision.')
pppSecuritySecretsDirection = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2,))).clone(namedValues=NamedValues(("local-to-remote", 1), ("remote-to-local", 2),))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppSecuritySecretsDirection.setDescription('This object defines the direction in which a\n                         particular ID/Secret pair is valid.  If this\n                         object is local-to-remote then the local PPP\n                         entity will use the ID/Secret pair when\n                         attempting to authenticate the local PPP entity\n                         to the remote PPP entity.  If this object is\n                         remote-to-local then the local PPP entity will\n                         expect the ID/Secret pair to be used by the\n                         remote PPP entity when the remote PPP entity\n                         attempts to authenticate itself to the local\n                         PPP entity.')
pppSecuritySecretsProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 4), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppSecuritySecretsProtocol.setDescription('The security protocol (e.g. CHAP or PAP) to\n                         which this ID/Secret pair applies.')
pppSecuritySecretsIdentity = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0,255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppSecuritySecretsIdentity.setDescription('The Identity of the ID/Secret pair.  The\n                         actual format, semantics, and use of\n                         pppSecuritySecretsIdentity depends on the\n                         actual security protocol used.  For example, if\n                         pppSecuritySecretsProtocol is\n                         pppSecurityPapProtocol then this object will\n                         contain a PAP Peer-ID. If\n                         pppSecuritySecretsProtocol is\n                         pppSecurityChapMD5Protocol then this object\n                         would contain the CHAP NAME parameter.')
pppSecuritySecretsSecret = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0,255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppSecuritySecretsSecret.setDescription('The secret of the ID/Secret pair.  The actual\n                         format, semantics, and use of\n                         pppSecuritySecretsSecret depends on the actual\n                         security protocol used.  For example, if\n                         pppSecuritySecretsProtocol is\n                         pppSecurityPapProtocol then this object will\n                         contain a PAP Password. If\n                         pppSecuritySecretsProtocol is\n                         pppSecurityChapMD5Protocol then this object\n                         would contain the CHAP MD5 Secret.')
pppSecuritySecretsStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2,))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2),)).clone('valid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppSecuritySecretsStatus.setDescription('Setting this object to the value invalid(1)\n                         has the effect of invalidating the\n                         corresponding entry in the\n                         pppSecuritySecretsTable. It is an\n                         implementation-specific matter as to whether\n                         the agent removes an invalidated entry from the\n                         table.  Accordingly, management stations must\n                         be prepared to receive tabular information from\n                         agents that corresponds to entries not\n                         currently in use.  Proper interpretation of\n                         such entries requires examination of the\n                         relevant pppSecuritySecretsStatus object.')
mibBuilder.exportSymbols("PPP-SEC-MIB", pppSecuritySecretsEntry=pppSecuritySecretsEntry, pppSecurityConfigLink=pppSecurityConfigLink, pppSecuritySecretsLink=pppSecuritySecretsLink, pppSecuritySecretsProtocol=pppSecuritySecretsProtocol, pppSecurity=pppSecurity, pppSecuritySecretsIdentity=pppSecuritySecretsIdentity, pppSecuritySecretsTable=pppSecuritySecretsTable, pppSecurityConfigEntry=pppSecurityConfigEntry, pppSecurityProtocols=pppSecurityProtocols, pppSecurityConfigTable=pppSecurityConfigTable, pppSecurityConfigPreference=pppSecurityConfigPreference, pppSecurityConfigStatus=pppSecurityConfigStatus, pppSecurityConfigProtocol=pppSecurityConfigProtocol, pppSecuritySecretsStatus=pppSecuritySecretsStatus, pppSecuritySecretsSecret=pppSecuritySecretsSecret, pppSecuritySecretsIdIndex=pppSecuritySecretsIdIndex, pppSecurityPapProtocol=pppSecurityPapProtocol, pppSecurityChapMD5Protocol=pppSecurityChapMD5Protocol, pppSecuritySecretsDirection=pppSecuritySecretsDirection)
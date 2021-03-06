api_names = [
    'org.zstack.appliancevm.APIQueryApplianceVmMsg',
    'org.zstack.storage.ceph.backup.APIRemoveMonFromCephBackupStorageMsg',
    'org.zstack.storage.ceph.backup.APIAddMonToCephBackupStorageMsg',
    'org.zstack.storage.ceph.backup.APIAddCephBackupStorageMsg',
    'org.zstack.storage.ceph.backup.APIQueryCephBackupStorageMsg',
    'org.zstack.storage.ceph.primary.APIQueryCephPrimaryStorageMsg',
    'org.zstack.storage.ceph.primary.APIRemoveMonFromCephPrimaryStorageMsg',
    'org.zstack.storage.ceph.primary.APIAddMonToCephPrimaryStorageMsg',
    'org.zstack.storage.ceph.primary.APIAddCephPrimaryStorageMsg',
    'org.zstack.core.config.APIGetGlobalConfigMsg',
    'org.zstack.core.config.APIUpdateGlobalConfigMsg',
    'org.zstack.core.config.APIQueryGlobalConfigMsg',
    'org.zstack.network.service.eip.APIDeleteEipMsg',
    'org.zstack.network.service.eip.APIDetachEipMsg',
    'org.zstack.network.service.eip.APIQueryEipMsg',
    'org.zstack.network.service.eip.APIChangeEipStateMsg',
    'org.zstack.network.service.eip.APIGetEipAttachableVmNicsMsg',
    'org.zstack.network.service.eip.APIAttachEipMsg',
    'org.zstack.network.service.eip.APICreateEipMsg',
    'org.zstack.network.service.eip.APIUpdateEipMsg',
    'org.zstack.storage.fusionstor.primary.APIAddFusionstorPrimaryStorageMsg',
    'org.zstack.storage.fusionstor.primary.APIAddMonToFusionstorPrimaryStorageMsg',
    'org.zstack.storage.fusionstor.primary.APIRemoveMonFromFusionstorPrimaryStorageMsg',
    'org.zstack.storage.fusionstor.primary.APIQueryFusionstorPrimaryStorageMsg',
    'org.zstack.storage.fusionstor.backup.APIAddMonToFusionstorBackupStorageMsg',
    'org.zstack.storage.fusionstor.backup.APIAddFusionstorBackupStorageMsg',
    'org.zstack.storage.fusionstor.backup.APIRemoveMonFromFusionstorBackupStorageMsg',
    'org.zstack.storage.fusionstor.backup.APIQueryFusionstorBackupStorageMsg',
    'org.zstack.header.storage.primary.APIQueryPrimaryStorageMsg',
    'org.zstack.header.storage.primary.APIGetPrimaryStorageCapacityMsg',
    'org.zstack.header.storage.primary.APISyncPrimaryStorageCapacityMsg',
    'org.zstack.header.storage.primary.APIDetachPrimaryStorageFromClusterMsg',
    'org.zstack.header.storage.primary.APIGetPrimaryStorageAllocatorStrategiesMsg',
    'org.zstack.header.storage.primary.APIReconnectPrimaryStorageMsg',
    'org.zstack.header.storage.primary.APIDeletePrimaryStorageMsg',
    'org.zstack.header.storage.primary.APIChangePrimaryStorageStateMsg',
    'org.zstack.header.storage.primary.APIUpdatePrimaryStorageMsg',
    'org.zstack.header.storage.primary.APIAttachPrimaryStorageToClusterMsg',
    'org.zstack.header.storage.primary.APIGetPrimaryStorageTypesMsg',
    'org.zstack.header.storage.snapshot.APIQueryVolumeSnapshotMsg',
    'org.zstack.header.storage.snapshot.APIBackupVolumeSnapshotMsg',
    'org.zstack.header.storage.snapshot.APIRevertVolumeFromSnapshotMsg',
    'org.zstack.header.storage.snapshot.APIGetVolumeSnapshotTreeMsg',
    'org.zstack.header.storage.snapshot.APIDeleteVolumeSnapshotMsg',
    'org.zstack.header.storage.snapshot.APIUpdateVolumeSnapshotMsg',
    'org.zstack.header.storage.snapshot.APIQueryVolumeSnapshotTreeMsg',
    'org.zstack.header.storage.snapshot.APIDeleteVolumeSnapshotFromBackupStorageMsg',
    'org.zstack.header.storage.backup.APIAttachBackupStorageToZoneMsg',
    'org.zstack.header.storage.backup.APIGetBackupStorageCapacityMsg',
    'org.zstack.header.storage.backup.APIDetachBackupStorageFromZoneMsg',
    'org.zstack.header.storage.backup.APIScanBackupStorageMsg',
    'org.zstack.header.storage.backup.APIUpdateBackupStorageMsg',
    'org.zstack.header.storage.backup.APIDeleteBackupStorageMsg',
    'org.zstack.header.storage.backup.APIReconnectBackupStorageMsg',
    'org.zstack.header.storage.backup.APIGetBackupStorageTypesMsg',
    'org.zstack.header.storage.backup.APIChangeBackupStorageStateMsg',
    'org.zstack.header.storage.backup.APIQueryBackupStorageMsg',
    'org.zstack.header.query.APIGenerateQueryableFieldsMsg',
    'org.zstack.header.query.APIGenerateInventoryQueryDetailsMsg',
    'org.zstack.header.message.APICreateMessage',
    'org.zstack.header.configuration.APICreateDiskOfferingMsg',
    'org.zstack.header.configuration.APIGenerateSqlForeignKeyMsg',
    'org.zstack.header.configuration.APIGenerateTestLinkDocumentMsg',
    'org.zstack.header.configuration.APIChangeDiskOfferingStateMsg',
    'org.zstack.header.configuration.APIDeleteDiskOfferingMsg',
    'org.zstack.header.configuration.APIGenerateApiJsonTemplateMsg',
    'org.zstack.header.configuration.APICreateInstanceOfferingMsg',
    'org.zstack.header.configuration.APIGenerateGroovyClassMsg',
    'org.zstack.header.configuration.APIQueryDiskOfferingMsg',
    'org.zstack.header.configuration.APIUpdateInstanceOfferingMsg',
    'org.zstack.header.configuration.APIGenerateApiTypeScriptDefinitionMsg',
    'org.zstack.header.configuration.APIDeleteInstanceOfferingMsg',
    'org.zstack.header.configuration.APIGenerateSqlVOViewMsg',
    'org.zstack.header.configuration.APIUpdateDiskOfferingMsg',
    'org.zstack.header.configuration.APIGetGlobalPropertyMsg',
    'org.zstack.header.configuration.APIQueryInstanceOfferingMsg',
    'org.zstack.header.configuration.APIChangeInstanceOfferingStateMsg',
    'org.zstack.header.configuration.APIGenerateSqlIndexMsg',
    'org.zstack.header.identity.APIRemoveUserFromGroupMsg',
    'org.zstack.header.identity.APIQueryAccountResourceRefMsg',
    'org.zstack.header.identity.APIDeleteUserGroupMsg',
    'org.zstack.header.identity.APIAttachPolicyToUserGroupMsg',
    'org.zstack.header.identity.APIUpdateAccountMsg',
    'org.zstack.header.identity.APIUpdateQuotaMsg',
    'org.zstack.header.identity.APIDeleteUserMsg',
    'org.zstack.header.identity.APIQueryUserGroupMsg',
    'org.zstack.header.identity.APIDeletePolicyMsg',
    'org.zstack.header.identity.APIShareResourceMsg',
    'org.zstack.header.identity.APIGetResourceAccountMsg',
    'org.zstack.header.identity.APIAttachPolicyToUserMsg',
    'org.zstack.header.identity.APIUpdateUserGroupMsg',
    'org.zstack.header.identity.APIChangeResourceOwnerMsg',
    'org.zstack.header.identity.APIUpdateUserMsg',
    'org.zstack.header.identity.APIQueryAccountMsg',
    'org.zstack.header.identity.APISessionMessage',
    'org.zstack.header.identity.APICreatePolicyMsg',
    'org.zstack.header.identity.APIQueryPolicyMsg',
    'org.zstack.header.identity.APIValidateSessionMsg',
    'org.zstack.header.identity.APIAttachPoliciesToUserMsg',
    'org.zstack.header.identity.APILogOutMsg',
    'org.zstack.header.identity.APIDetachPolicyFromUserGroupMsg',
    'org.zstack.header.identity.APIDeleteAccountMsg',
    'org.zstack.header.identity.APIQueryQuotaMsg',
    'org.zstack.header.identity.APILogInByUserMsg',
    'org.zstack.header.identity.APIGetAccountQuotaUsageMsg',
    'org.zstack.header.identity.APIQueryUserMsg',
    'org.zstack.header.identity.APILogInByAccountMsg',
    'org.zstack.header.identity.APICreateUserGroupMsg',
    'org.zstack.header.identity.APIQuerySharedResourceMsg',
    'org.zstack.header.identity.APIDetachPolicyFromUserMsg',
    'org.zstack.header.identity.APICreateAccountMsg',
    'org.zstack.header.identity.APICreateUserMsg',
    'org.zstack.header.identity.APIDetachPoliciesFromUserMsg',
    'org.zstack.header.identity.APIRevokeResourceSharingMsg',
    'org.zstack.header.identity.APIAddUserToGroupMsg',
    'org.zstack.header.identity.APICheckApiPermissionMsg',
    'org.zstack.header.tag.APICreateSystemTagMsg',
    'org.zstack.header.tag.APICreateUserTagMsg',
    'org.zstack.header.tag.APIQuerySystemTagMsg',
    'org.zstack.header.tag.APIUpdateSystemTagMsg',
    'org.zstack.header.tag.APIQueryUserTagMsg',
    'org.zstack.header.tag.APIQueryTagMsg',
    'org.zstack.header.tag.APIDeleteTagMsg',
    'org.zstack.header.vm.APIGetVmBootOrderMsg',
    'org.zstack.header.vm.APIRebootVmInstanceMsg',
    'org.zstack.header.vm.APIRecoverVmInstanceMsg',
    'org.zstack.header.vm.APIGetVmAttachableL3NetworkMsg',
    'org.zstack.header.vm.APISetVmBootOrderMsg',
    'org.zstack.header.vm.APIChangeInstanceOfferingMsg',
    'org.zstack.header.vm.APIUpdateVmInstanceMsg',
    'org.zstack.header.vm.APIGetVmStartingCandidateClustersHostsMsg',
    'org.zstack.header.vm.APIDeleteVmStaticIpMsg',
    'org.zstack.header.vm.APIGetVmCapabilitiesMsg',
    'org.zstack.header.vm.APIGetVmConsoleAddressMsg',
    'org.zstack.header.vm.APIAttachL3NetworkToVmMsg',
    'org.zstack.header.vm.APIDestroyVmInstanceMsg',
    'org.zstack.header.vm.APIGetVmAttachableDataVolumeMsg',
    'org.zstack.header.vm.APIGetVmMigrationCandidateHostsMsg',
    'org.zstack.header.vm.APIQueryVmNicMsg',
    'org.zstack.header.vm.APIStopVmInstanceMsg',
    'org.zstack.header.vm.APIAttachIsoToVmInstanceMsg',
    'org.zstack.header.vm.APICreateVmInstanceMsg',
    'org.zstack.header.vm.APIExpungeVmInstanceMsg',
    'org.zstack.header.vm.APIDetachIsoFromVmInstanceMsg',
    'org.zstack.header.vm.APIMigrateVmMsg',
    'org.zstack.header.vm.APISetVmStaticIpMsg',
    'org.zstack.header.vm.APIGetVmHostnameMsg',
    'org.zstack.header.vm.APIQueryVmInstanceMsg',
    'org.zstack.header.vm.APISetVmHostnameMsg',
    'org.zstack.header.vm.APIStartVmInstanceMsg',
    'org.zstack.header.vm.APIDeleteVmHostnameMsg',
    'org.zstack.header.vm.APIDetachL3NetworkFromVmMsg',
    'org.zstack.header.volume.APIDeleteDataVolumeMsg',
    'org.zstack.header.volume.APIRecoverDataVolumeMsg',
    'org.zstack.header.volume.APIGetVolumeCapabilitiesMsg',
    'org.zstack.header.volume.APIBackupDataVolumeMsg',
    'org.zstack.header.volume.APICreateDataVolumeMsg',
    'org.zstack.header.volume.APIGetDataVolumeAttachableVmMsg',
    'org.zstack.header.volume.APIExpungeDataVolumeMsg',
    'org.zstack.header.volume.APIDetachDataVolumeFromVmMsg',
    'org.zstack.header.volume.APIQueryVolumeMsg',
    'org.zstack.header.volume.APICreateDataVolumeFromVolumeTemplateMsg',
    'org.zstack.header.volume.APIGetVolumeFormatMsg',
    'org.zstack.header.volume.APIAttachDataVolumeToVmMsg',
    'org.zstack.header.volume.APICreateVolumeSnapshotMsg',
    'org.zstack.header.volume.APISyncVolumeSizeMsg',
    'org.zstack.header.volume.APIUpdateVolumeMsg',
    'org.zstack.header.volume.APIChangeVolumeStateMsg',
    'org.zstack.header.volume.APICreateDataVolumeFromVolumeSnapshotMsg',
    'org.zstack.header.search.APISearchGenerateSqlTriggerMsg',
    'org.zstack.header.search.APIDeleteSearchIndexMsg',
    'org.zstack.header.search.APICreateSearchIndexMsg',
    'org.zstack.header.network.l3.APIAddIpRangeMsg',
    'org.zstack.header.network.l3.APIAddIpRangeByNetworkCidrMsg',
    'org.zstack.header.network.l3.APIGetIpAddressCapacityMsg',
    'org.zstack.header.network.l3.APIUpdateIpRangeMsg',
    'org.zstack.header.network.l3.APIUpdateL3NetworkMsg',
    'org.zstack.header.network.l3.APICreateL3NetworkMsg',
    'org.zstack.header.network.l3.APIAddDnsToL3NetworkMsg',
    'org.zstack.header.network.l3.APIDeleteIpRangeMsg',
    'org.zstack.header.network.l3.APIRemoveDnsFromL3NetworkMsg',
    'org.zstack.header.network.l3.APIGetL3NetworkTypesMsg',
    'org.zstack.header.network.l3.APIGetFreeIpMsg',
    'org.zstack.header.network.l3.APIQueryIpRangeMsg',
    'org.zstack.header.network.l3.APIDeleteL3NetworkMsg',
    'org.zstack.header.network.l3.APIChangeL3NetworkStateMsg',
    'org.zstack.header.network.l3.APICheckIpAvailabilityMsg',
    'org.zstack.header.network.l3.APIQueryL3NetworkMsg',
    'org.zstack.header.network.service.APIQueryNetworkServiceL3NetworkRefMsg',
    'org.zstack.header.network.service.APIAttachNetworkServiceProviderToL2NetworkMsg',
    'org.zstack.header.network.service.APIDetachNetworkServiceProviderFromL2NetworkMsg',
    'org.zstack.header.network.service.APIGetNetworkServiceTypesMsg',
    'org.zstack.header.network.service.APIQueryNetworkServiceProviderMsg',
    'org.zstack.header.network.service.APIAddNetworkServiceProviderMsg',
    'org.zstack.header.network.service.APIAttachNetworkServiceToL3NetworkMsg',
    'org.zstack.header.network.service.APIDetachNetworkServiceFromL3NetworkMsg',
    'org.zstack.header.network.l2.APIGetL2NetworkTypesMsg',
    'org.zstack.header.network.l2.APICreateL2NoVlanNetworkMsg',
    'org.zstack.header.network.l2.APIAttachL2NetworkToClusterMsg',
    'org.zstack.header.network.l2.APIUpdateL2NetworkMsg',
    'org.zstack.header.network.l2.APIDeleteL2NetworkMsg',
    'org.zstack.header.network.l2.APIDetachL2NetworkFromClusterMsg',
    'org.zstack.header.network.l2.APIQueryL2NetworkMsg',
    'org.zstack.header.network.l2.APICreateL2VlanNetworkMsg',
    'org.zstack.header.network.l2.APIQueryL2VlanNetworkMsg',
    'org.zstack.header.host.APIGetHypervisorTypesMsg',
    'org.zstack.header.host.APIDeleteHostMsg',
    'org.zstack.header.host.APIChangeHostStateMsg',
    'org.zstack.header.host.APIQueryHostMsg',
    'org.zstack.header.host.APIReconnectHostMsg',
    'org.zstack.header.host.APIUpdateHostMsg',
    'org.zstack.header.image.APIAddImageMsg',
    'org.zstack.header.image.APIUpdateImageMsg',
    'org.zstack.header.image.APICreateDataVolumeTemplateFromVolumeMsg',
    'org.zstack.header.image.APIRecoverImageMsg',
    'org.zstack.header.image.APIChangeImageStateMsg',
    'org.zstack.header.image.APIExpungeImageMsg',
    'org.zstack.header.image.APICreateRootVolumeTemplateFromRootVolumeMsg',
    'org.zstack.header.image.APIDeleteImageMsg',
    'org.zstack.header.image.APISyncImageSizeMsg',
    'org.zstack.header.image.APIQueryImageMsg',
    'org.zstack.header.image.APICreateRootVolumeTemplateFromVolumeSnapshotMsg',
    'org.zstack.header.allocator.APIGetCpuMemoryCapacityMsg',
    'org.zstack.header.allocator.APIGetHostAllocatorStrategiesMsg',
    'org.zstack.header.zone.APIChangeZoneStateMsg',
    'org.zstack.header.zone.APIDeleteZoneMsg',
    'org.zstack.header.zone.APIQueryZoneMsg',
    'org.zstack.header.zone.APICreateZoneMsg',
    'org.zstack.header.zone.APIUpdateZoneMsg',
    'org.zstack.header.cluster.APICreateClusterMsg',
    'org.zstack.header.cluster.APIDeleteClusterMsg',
    'org.zstack.header.cluster.APIChangeClusterStateMsg',
    'org.zstack.header.cluster.APIUpdateClusterMsg',
    'org.zstack.header.cluster.APIQueryClusterMsg',
    'org.zstack.header.managementnode.APIQueryManagementNodeMsg',
    'org.zstack.header.managementnode.APIGetVersionMsg',
    'org.zstack.header.console.APIReconnectConsoleProxyAgentMsg',
    'org.zstack.header.console.APIRequestConsoleAccessMsg',
    'org.zstack.header.console.APIQueryConsoleProxyAgentMsg',
    'org.zstack.header.apimediator.APIIsReadyToGoMsg',
    'org.zstack.kvm.APIAddKVMHostMsg',
    'org.zstack.kvm.APIUpdateKVMHostMsg',
    'org.zstack.kvm.APIKvmRunShellMsg',
    'org.zstack.network.service.lb.APIRefreshLoadBalancerMsg',
    'org.zstack.network.service.lb.APIQueryLoadBalancerListenerMsg',
    'org.zstack.network.service.lb.APIQueryLoadBalancerMsg',
    'org.zstack.network.service.lb.APICreateLoadBalancerListenerMsg',
    'org.zstack.network.service.lb.APIDeleteLoadBalancerMsg',
    'org.zstack.network.service.lb.APIAddVmNicToLoadBalancerMsg',
    'org.zstack.network.service.lb.APICreateLoadBalancerMsg',
    'org.zstack.network.service.lb.APIDeleteLoadBalancerListenerMsg',
    'org.zstack.network.service.lb.APIRemoveVmNicFromLoadBalancerMsg',
    'org.zstack.storage.primary.local.APILocalStorageMigrateVolumeMsg',
    'org.zstack.storage.primary.local.APILocalStorageGetVolumeMigratableHostsMsg',
    'org.zstack.storage.primary.local.APIGetLocalStorageHostDiskCapacityMsg',
    'org.zstack.storage.primary.local.APIAddLocalPrimaryStorageMsg',
    'org.zstack.storage.primary.local.APIQueryLocalStorageResourceRefMsg',
    'org.zstack.storage.primary.nfs.APIAddNfsPrimaryStorageMsg',
    'org.zstack.network.service.portforwarding.APIDeletePortForwardingRuleMsg',
    'org.zstack.network.service.portforwarding.APIGetPortForwardingAttachableVmNicsMsg',
    'org.zstack.network.service.portforwarding.APIChangePortForwardingRuleStateMsg',
    'org.zstack.network.service.portforwarding.APIDetachPortForwardingRuleMsg',
    'org.zstack.network.service.portforwarding.APIAttachPortForwardingRuleMsg',
    'org.zstack.network.service.portforwarding.APICreatePortForwardingRuleMsg',
    'org.zstack.network.service.portforwarding.APIQueryPortForwardingRuleMsg',
    'org.zstack.network.service.portforwarding.APIUpdatePortForwardingRuleMsg',
    'org.zstack.network.securitygroup.APICreateSecurityGroupMsg',
    'org.zstack.network.securitygroup.APIUpdateSecurityGroupMsg',
    'org.zstack.network.securitygroup.APIQuerySecurityGroupRuleMsg',
    'org.zstack.network.securitygroup.APIQueryVmNicInSecurityGroupMsg',
    'org.zstack.network.securitygroup.APIDeleteSecurityGroupMsg',
    'org.zstack.network.securitygroup.APIAttachSecurityGroupToL3NetworkMsg',
    'org.zstack.network.securitygroup.APIDeleteVmNicFromSecurityGroupMsg',
    'org.zstack.network.securitygroup.APIGetCandidateVmNicForSecurityGroupMsg',
    'org.zstack.network.securitygroup.APIDetachSecurityGroupFromL3NetworkMsg',
    'org.zstack.network.securitygroup.APIAddSecurityGroupRuleMsg',
    'org.zstack.network.securitygroup.APIDeleteSecurityGroupRuleMsg',
    'org.zstack.network.securitygroup.APIAddVmNicToSecurityGroupMsg',
    'org.zstack.network.securitygroup.APIChangeSecurityGroupStateMsg',
    'org.zstack.network.securitygroup.APIQuerySecurityGroupMsg',
    'org.zstack.storage.backup.sftp.APIReconnectSftpBackupStorageMsg',
    'org.zstack.storage.backup.sftp.APIQuerySftpBackupStorageMsg',
    'org.zstack.storage.backup.sftp.APIAddSftpBackupStorageMsg',
    'org.zstack.storage.backup.sftp.APIUpdateSftpBackupStorageMsg',
    'org.zstack.storage.primary.smp.APIAddSharedMountPointPrimaryStorageMsg',
    'org.zstack.header.simulator.APIAddSimulatorHostMsg',
    'org.zstack.header.simulator.storage.backup.APIAddSimulatorBackupStorageMsg',
    'org.zstack.header.simulator.storage.primary.APIAddSimulatorPrimaryStorageMsg',
    'org.zstack.network.service.vip.APICreateVipMsg',
    'org.zstack.network.service.vip.APIUpdateVipMsg',
    'org.zstack.network.service.vip.APIQueryVipMsg',
    'org.zstack.network.service.vip.APIChangeVipStateMsg',
    'org.zstack.network.service.vip.APIDeleteVipMsg',
    'org.zstack.network.service.virtualrouter.APICreateVirtualRouterOfferingMsg',
    'org.zstack.network.service.virtualrouter.APIUpdateVirtualRouterOfferingMsg',
    'org.zstack.network.service.virtualrouter.APIQueryVirtualRouterOfferingMsg',
    'org.zstack.network.service.virtualrouter.APICreateVirtualRouterVmMsg',
    'org.zstack.network.service.virtualrouter.APIReconnectVirtualRouterMsg',
    'org.zstack.network.service.virtualrouter.APIQueryVirtualRouterVmMsg',
]

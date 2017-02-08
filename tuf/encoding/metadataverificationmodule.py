# Auto-generated by asn1ate v.0.5.1.dev from metadataverificationmodule.asn1
# (last modified on 2017-01-30 17:00:01.841176)

from pyasn1.type import univ, char, namedtype, namedval, tag, constraint, useful

# To make this module work, had to:
# 1. Define the INTEGER MAX value.
# https://www.obj-sys.com/docs/acv58/CCppUsersGuide/CCppUsersGuidea12.html
MAX = 2**32-1

class OctetString(univ.OctetString):
    pass


OctetString.subtypeSpec = constraint.ValueSizeConstraint(1, 1024)


class BitString(univ.BitString):
    pass


BitString.subtypeSpec=constraint.ValueSizeConstraint(1, 1024)


class BinaryData(univ.Choice):
    pass


BinaryData.componentType = namedtype.NamedTypes(
    namedtype.NamedType('bitString', BitString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.NamedType('octetString', OctetString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))
)


class EncryptedSymmetricKeyType(univ.Enumerated):
    pass


EncryptedSymmetricKeyType.namedValues = namedval.NamedValues(
    ('aes128', 0),
    ('aes192', 1),
    ('aes256', 2)
)


class EncryptedSymmetricKey(univ.Sequence):
    pass


EncryptedSymmetricKey.componentType = namedtype.NamedTypes(
    namedtype.NamedType('encryptedSymmetricKeyType', EncryptedSymmetricKeyType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.NamedType('encryptedSymmetricKeyValue', BinaryData().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))
)


class Identifier(char.VisibleString):
    pass


Identifier.subtypeSpec = constraint.ValueSizeConstraint(1, 32)


class Natural(univ.Integer):
    pass


Natural.subtypeSpec = constraint.ValueRangeConstraint(0, MAX)


class Positive(univ.Integer):
    pass


Positive.subtypeSpec = constraint.ValueRangeConstraint(1, MAX)


class Length(Natural):
    pass


class HashFunction(univ.Enumerated):
    pass


HashFunction.namedValues = namedval.NamedValues(
    ('sha224', 0),
    ('sha256', 1),
    ('sha384', 2),
    ('sha512', 3),
    ('sha512-224', 4),
    ('sha512-256', 5)
)


class Hash(univ.Sequence):
    pass


Hash.componentType = namedtype.NamedTypes(
    namedtype.NamedType('function', HashFunction().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.NamedType('digest', BinaryData().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))
)


class Hashes(univ.SequenceOf):
    pass


Hashes.componentType = Hash()
Hashes.subtypeSpec=constraint.ValueSizeConstraint(1, 8)


class Filename(char.VisibleString):
    pass


Filename.subtypeSpec = constraint.ValueSizeConstraint(1, 32)


class Target(univ.Sequence):
    pass


Target.componentType = namedtype.NamedTypes(
    namedtype.NamedType('filename', Filename().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.NamedType('length', Length().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
    namedtype.NamedType('numberOfHashes', Length().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
    namedtype.NamedType('hashes', Hashes().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3)))
)


class Custom(univ.Sequence):
    pass


Custom.componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('releaseCounter', Natural().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.OptionalNamedType('hardwareIdentifier', Identifier().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
    namedtype.OptionalNamedType('ecuIdentifier', Identifier().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
    namedtype.OptionalNamedType('encryptedTarget', Target().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('encryptedSymmetricKey', EncryptedSymmetricKey().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)))
)


class Keyid(BinaryData):
    pass


class Keyids(univ.SequenceOf):
    pass


Keyids.componentType = Keyid()
Keyids.subtypeSpec=constraint.ValueSizeConstraint(1, 8)


class StrictFilename(char.VisibleString):
    pass


StrictFilename.subtypeSpec = constraint.ValueSizeConstraint(1, 32)


class RepositoryName(StrictFilename):
    pass


class URL(char.VisibleString):
    pass


URL.subtypeSpec = constraint.ValueSizeConstraint(1, 1024)


class URLs(univ.SequenceOf):
    pass


URLs.componentType = URL()
URLs.subtypeSpec=constraint.ValueSizeConstraint(0, 8)


class Repository(univ.Sequence):
    pass


Repository.componentType = namedtype.NamedTypes(
    namedtype.NamedType('name', RepositoryName().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.NamedType('numberOfServers', Length().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
    namedtype.NamedType('servers', URLs().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))
)


class Repositories(univ.SequenceOf):
    pass


Repositories.componentType = Repository()
Repositories.subtypeSpec=constraint.ValueSizeConstraint(2, 2)


class Path(char.VisibleString):
    pass


Path.subtypeSpec = constraint.ValueSizeConstraint(1, 32)


class Paths(univ.SequenceOf):
    pass


Paths.componentType = Path()
Paths.subtypeSpec=constraint.ValueSizeConstraint(1, 8)


class RepositoryNames(univ.SequenceOf):
    pass


RepositoryNames.componentType = RepositoryName()
RepositoryNames.subtypeSpec=constraint.ValueSizeConstraint(2, 2)


class Mapping(univ.Sequence):
    pass


Mapping.componentType = namedtype.NamedTypes(
    namedtype.NamedType('numberOfPaths', Length().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.NamedType('paths', Paths().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
    namedtype.NamedType('numberOfRepositories', Length().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
    namedtype.NamedType('repositories', RepositoryNames().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
    namedtype.DefaultedNamedType('terminating', univ.Boolean().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4)).subtype(value=0))
)


class Mappings(univ.SequenceOf):
    pass


Mappings.componentType = Mapping()
Mappings.subtypeSpec=constraint.ValueSizeConstraint(1, 1)


class MapFile(univ.Sequence):
    pass


MapFile.componentType = namedtype.NamedTypes(
    namedtype.NamedType('numberOfRepositories', Length().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.NamedType('repositories', Repositories().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
    namedtype.NamedType('numberOfMappings', Length().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
    namedtype.NamedType('mappings', Mappings().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3)))
)


class SignatureMethod(univ.Enumerated):
    pass


SignatureMethod.namedValues = namedval.NamedValues(
    ('rsassa-pss', 0),
    ('ed25519', 1)
)


class Signature(univ.Sequence):
    pass


Signature.componentType = namedtype.NamedTypes(
    namedtype.NamedType('keyid', Keyid().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.NamedType('method', SignatureMethod().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
    #namedtype.NamedType('hash', Hash().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.NamedType('value', BinaryData().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)))
)


class Signatures(univ.SequenceOf):
    pass


Signatures.componentType = Signature()
Signatures.subtypeSpec=constraint.ValueSizeConstraint(1, 8)


class RoleType(univ.Enumerated):
    pass


RoleType.namedValues = namedval.NamedValues(
    ('root', 0),
    ('targets', 1),
    ('snapshot', 2),
    ('timestamp', 3)
)


class UTCDateTime(Positive):
    pass


# The next class, 'Version', should ideally inherit from class Positive instead
# of Natural; however there is a point during the initial write of metadata
# during which the version may be 0 and signature checks may occur, in which
# case conversions must succeed - so we allow 0 for version, but do not expect
# a version 0 to be final / written to disk / transmitted.
class Version(Natural): # Should be positive, but TUF has a certain point during an initial write during which the version is 0 and signature checks may still occur, in which case conversions must succeed.
    pass


class SnapshotMetadataFile(univ.Sequence):
    pass


SnapshotMetadataFile.componentType = namedtype.NamedTypes(
    namedtype.NamedType('filename', StrictFilename().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.NamedType('version', Version().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))
)


class SnapshotMetadataFiles(univ.SequenceOf):
    pass


SnapshotMetadataFiles.componentType = SnapshotMetadataFile()
SnapshotMetadataFiles.subtypeSpec=constraint.ValueSizeConstraint(1, 128)


class SnapshotMetadata(univ.Sequence):
    pass


SnapshotMetadata.componentType = namedtype.NamedTypes(
    namedtype.NamedType('numberOfSnapshotMetadataFiles', Length().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.NamedType('snapshotMetadataFiles', SnapshotMetadataFiles().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))
)


class PublicKeyType(univ.Enumerated):
    pass


PublicKeyType.namedValues = namedval.NamedValues(
    ('rsa', 0),
    ('ed25519', 1)
)


class PublicKey(univ.Sequence):
    pass


PublicKey.componentType = namedtype.NamedTypes(
    namedtype.NamedType('publicKeyid', Keyid().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.NamedType('publicKeyType', PublicKeyType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
    namedtype.NamedType('publicKeyValue', BinaryData().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)))
)


class PublicKeys(univ.SequenceOf):
    pass


PublicKeys.componentType = PublicKey()
PublicKeys.subtypeSpec=constraint.ValueSizeConstraint(1, 8)


class Threshold(Positive):
    pass


class TopLevelRole(univ.Sequence):
    pass


TopLevelRole.componentType = namedtype.NamedTypes(
    namedtype.NamedType('role', RoleType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.OptionalNamedType('numberOfURLs', Length().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
    namedtype.OptionalNamedType('urls', URLs().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
    namedtype.NamedType('numberOfKeyids', Length().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
    namedtype.NamedType('keyids', Keyids().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
    namedtype.NamedType('threshold', Threshold().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5)))
)


class TopLevelRoles(univ.SequenceOf):
    pass


TopLevelRoles.componentType = TopLevelRole()
TopLevelRoles.subtypeSpec=constraint.ValueSizeConstraint(4, 4)


class RootMetadata(univ.Sequence):
    pass


RootMetadata.componentType = namedtype.NamedTypes(
    namedtype.NamedType('numberOfKeys', Length().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.NamedType('keys', PublicKeys().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
    namedtype.NamedType('numberOfRoles', Length().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
    namedtype.NamedType('roles', TopLevelRoles().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3)))
)


class TimestampMetadata(univ.Sequence):
    pass


TimestampMetadata.componentType = namedtype.NamedTypes(
    namedtype.NamedType('filename', Filename().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.NamedType('version', Version().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
    namedtype.NamedType('length', Length().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
    namedtype.NamedType('numberOfHashes', Length().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
    namedtype.NamedType('hashes', Hashes().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4)))
)


class MultiRole(univ.Sequence):
    pass


MultiRole.componentType = namedtype.NamedTypes(
    namedtype.NamedType('rolename', StrictFilename().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.NamedType('numberOfKeyids', Length().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
    namedtype.NamedType('keyids', Keyids().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
    namedtype.NamedType('threshold', Threshold().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3)))
)


class MultiRoles(univ.SequenceOf):
    pass


MultiRoles.componentType = MultiRole()
MultiRoles.subtypeSpec=constraint.ValueSizeConstraint(1, 8)


class PathsToRoles(univ.Sequence):
    pass


PathsToRoles.componentType = namedtype.NamedTypes(
    namedtype.NamedType('numberOfPaths', Length().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.NamedType('paths', Paths().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
    namedtype.NamedType('numberOfRoles', Length().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
    namedtype.NamedType('roles', MultiRoles().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
    namedtype.DefaultedNamedType('terminating', univ.Boolean().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4)).subtype(value=0))
)


class PrioritizedPathsToRoles(univ.SequenceOf):
    pass


PrioritizedPathsToRoles.componentType = PathsToRoles()
PrioritizedPathsToRoles.subtypeSpec=constraint.ValueSizeConstraint(1, 8)


class TargetsDelegations(univ.Sequence):
    pass


TargetsDelegations.componentType = namedtype.NamedTypes(
    namedtype.NamedType('numberOfKeys', Length().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.NamedType('keys', PublicKeys().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
    namedtype.NamedType('numberOfDelegations', Length().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
    namedtype.NamedType('delegations', PrioritizedPathsToRoles().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3)))
)


class TargetAndCustom(univ.Sequence):
    pass


TargetAndCustom.componentType = namedtype.NamedTypes(
    namedtype.NamedType('target', Target().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('custom', Custom().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))
)


class Targets(univ.SequenceOf):
    pass


Targets.componentType = TargetAndCustom()
Targets.subtypeSpec=constraint.ValueSizeConstraint(1, 128)


class TargetsMetadata(univ.Sequence):
    pass


TargetsMetadata.componentType = namedtype.NamedTypes(
    namedtype.NamedType('numberOfTargets', Natural().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.NamedType('targets', Targets().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
    namedtype.OptionalNamedType('delegations', TargetsDelegations().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)))
)


class SignedBody(univ.Choice):
    pass


SignedBody.componentType = namedtype.NamedTypes(
    namedtype.NamedType('rootMetadata', RootMetadata().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.NamedType('targetsMetadata', TargetsMetadata().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.NamedType('snapshotMetadata', SnapshotMetadata().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.NamedType('timestampMetadata', TimestampMetadata().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)))
)


class Signed(univ.Sequence):
    pass


Signed.componentType = namedtype.NamedTypes(
    namedtype.NamedType('type', RoleType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.NamedType('expires', UTCDateTime().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
    # The next field, 'version', should ideally use Positive() instead of
    # Natural(); however there is a point during the initial write of metadata
    # during which the version may be 0 and signature checks may occur, in
    # which case conversions must succeed - so we allow 0 for version, but
    # do not expect a version 0 to be final / written to disk / transmitted.
    namedtype.NamedType('version', Natural().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
    namedtype.NamedType('body', SignedBody().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)))
)


class Metadata(univ.Sequence):
    pass


Metadata.componentType = namedtype.NamedTypes(
    namedtype.NamedType('signed', Signed().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.NamedType('numberOfSignatures', Length().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
    namedtype.NamedType('signatures', Signatures().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))
)

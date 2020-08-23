import semver

old_version = semver.VersionInfo.parse(open('.version').read())
new_version = f'{old_version.major}.{old_version.minor}.{old_version.patch+1}'

with open(".version", 'w') as writer:
    writer.write(new_version)

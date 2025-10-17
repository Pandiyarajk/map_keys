# Deployment Guide - Key Mapper

## Quick Deployment Checklist

### Prerequisites
- [ ] Windows OS (7/8/10/11)
- [ ] Python 3.8+ installed (for building from source)
- [ ] Git installed (for cloning repository)
- [ ] Administrator privileges

### Deployment Steps

#### Option 1: Deploy Pre-built Executable (Recommended for End Users)

1. **Build the executable** (one-time)
   ```bash
   git clone <repository-url>
   cd map_keys
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   python build.py
   ```

2. **Distribute the package**
   - Package location: `distribution/`
   - Contains:
     - `KeyMapper.exe`
     - `README.md`
     - `CHANGE_LOG.md`
     - `key_mappings.json.sample`

3. **User Installation**
   - User downloads the distribution package
   - Extracts to desired location
   - Runs `KeyMapper.exe` as administrator
   - Done!

#### Option 2: GitHub Release (Automated)

1. **Create a release tag**
   ```bash
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```

2. **GitHub Actions automatically**:
   - Builds the application
   - Runs tests
   - Creates release
   - Uploads `KeyMapper.exe`

3. **Users download** from:
   - GitHub Releases page
   - Direct download link

#### Option 3: Deploy from Source (For Developers)

1. **Users clone repository**
   ```bash
   git clone <repository-url>
   cd map_keys
   ```

2. **Run setup**
   ```bash
   setup.bat
   ```

3. **Run application**
   ```bash
   run.bat
   ```

## Distribution Channels

### 1. GitHub Releases (Primary)
- **Pros**: Free, automatic via CI/CD, version tracking
- **Cons**: Requires GitHub account for advanced features
- **Best for**: Open source distribution

### 2. Direct Download (Website)
- **Pros**: Simple, no account needed
- **Cons**: Manual upload process
- **Best for**: Personal website distribution

### 3. Windows Store (Future)
- **Pros**: Official distribution, auto-updates
- **Cons**: Requires developer account ($), review process
- **Best for**: Maximum reach

### 4. Microsoft Store (Future)
- **Pros**: Built-in updater, trusted source
- **Cons**: Packaging requirements, certification
- **Best for**: Professional distribution

## Deployment Environments

### Development
```bash
# Local development
git clone <repo>
cd map_keys
setup.bat
run.bat
```

### Testing/Staging
```bash
# Build and test
python build.py
cd distribution
KeyMapper.exe
```

### Production
```bash
# Create release
git tag -a v1.0.0 -m "Production release"
git push origin v1.0.0
# GitHub Actions handles the rest
```

## Update Deployment

### For Users (Manual Update)
1. Download new version
2. Replace old `KeyMapper.exe`
3. Keep existing `key_mappings.json`

### For Users (Automatic Update - Future)
- Planned: In-app update checker
- Downloads new version
- Preserves configuration

## Rollback Procedure

### If Issues Occur
1. Download previous version from releases
2. Replace current `KeyMapper.exe`
3. Restart application

### Emergency Rollback
```bash
# Revert to previous tag
git checkout v1.0.0
python build.py
```

## Monitoring & Feedback

### User Feedback Channels
1. GitHub Issues
2. Email support
3. User surveys

### Metrics to Track
- Download count
- Issue reports
- Feature requests
- User testimonials

## Security Considerations

### Before Deployment
- [ ] Code reviewed
- [ ] Tests passing
- [ ] No hardcoded credentials
- [ ] Dependencies up to date
- [ ] Antivirus scanned

### Distribution Security
- [ ] HTTPS for downloads
- [ ] Checksum provided (future)
- [ ] Digital signature (future)
- [ ] Virus scan certificates

## Post-Deployment Tasks

### Immediately After Release
- [ ] Test download link
- [ ] Verify executable works
- [ ] Update website/documentation
- [ ] Announce on social media
- [ ] Monitor for issues

### First Week
- [ ] Check for bug reports
- [ ] Respond to issues
- [ ] Gather feedback
- [ ] Plan hotfix if needed

### First Month
- [ ] Review usage metrics
- [ ] Collect feature requests
- [ ] Plan next version
- [ ] Update roadmap

## Troubleshooting Deployment

### Build Fails
- Check Python version
- Update dependencies
- Clean build directory
- Check antivirus settings

### Users Can't Run Executable
- Verify Windows version
- Check antivirus blocks
- Ensure admin rights
- Check system requirements

### GitHub Actions Fails
- Check workflow syntax
- Verify secrets configured
- Review action logs
- Test locally first

## Best Practices

### Versioning
- Use semantic versioning (MAJOR.MINOR.PATCH)
- Tag all releases
- Maintain CHANGE_LOG.md

### Communication
- Clear release notes
- Migration guides for breaking changes
- Advance notice for deprecations

### Quality Assurance
- Test on multiple Windows versions
- Verify all features work
- Check for regressions
- User acceptance testing

## Future Deployment Enhancements

### Planned
- [ ] Auto-update feature
- [ ] Digital signing
- [ ] MSI installer
- [ ] Portable version
- [ ] Update notifications
- [ ] Crash reporting
- [ ] Usage analytics (opt-in)

## Support & Maintenance

### Regular Maintenance
- Weekly: Check issues
- Monthly: Security updates
- Quarterly: Feature releases
- Yearly: Major version

### End of Life Policy
- Support last 2 major versions
- Security patches for 1 year
- 6-month deprecation notice

---

**Deployment Status**: ✅ Ready for Production

**Last Updated**: 2025-10-17
**Version**: 1.0.0

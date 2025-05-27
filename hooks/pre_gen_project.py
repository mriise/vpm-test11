#!/usr/bin/env python3
"""Pre-generation hook for VPM package cookiecutter template."""

import re
import sys
from typing import Dict, Any

def validate_package_name(value: str) -> bool:
    """Validate reverse domain package name."""
    pattern = r'^[a-z][a-z0-9\-]*(\.[a-z0-9][a-z0-9\-]*)+$'
    return bool(re.match(pattern, value))

def validate_version(value: str) -> bool:
    """Validate semantic version."""
    pattern = r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$'
    return bool(re.match(pattern, value))

def validate_email(value: str) -> bool:
    """Validate email format (empty allowed)."""
    if not value:
        return True
    pattern = r'^[^@\s]+@[^@\s]+\.[^@\s]+$'
    return bool(re.match(pattern, value))

def validate_url(value: str) -> bool:
    """Validate HTTP/HTTPS URL (empty allowed)."""
    if not value:
        return True
    pattern = r'^https?://[^\s]+$'
    return bool(re.match(pattern, value))

def validate_unity_version(value: str) -> bool:
    """Validate Unity version format."""
    pattern = r'^((20\d{2}|[1-9]\d*)\.(0|[1-9]\d*)|([6-9]|[1-9]\d+)\.(0|[1-9]\d*))$'
    return bool(re.match(pattern, value))

def validate_github_url(value: str) -> bool:
    """Validate GitHub repository URL."""
    pattern = r'^https://github\.com/[^/]+/[^/]+$'
    return bool(re.match(pattern, value))

def main():
    """Validate cookiecutter context variables."""
    # Get cookiecutter context
    package_name = "{{ cookiecutter.package_name }}"
    display_name = "{{ cookiecutter.display_name }}"
    version = "{{ cookiecutter.version }}"
    description = "{{ cookiecutter.description }}"
    author_name = "{{ cookiecutter.author_name }}"
    author_email = "{{ cookiecutter.author_email }}"
    author_url = "{{ cookiecutter.author_url }}"
    unity_version = "{{ cookiecutter.unity_version }}"
    repo_url = "{{ cookiecutter.repo_url }}"
    
    errors = []
    
    # Validate package_name
    if not package_name:
        errors.append("package_name is required")
    elif not validate_package_name(package_name):
        errors.append("package_name must use lowercase reverse domain notation with dots")
    
    # Validate display_name
    if not display_name:
        errors.append("display_name is required")
    elif len(display_name) > 50:
        errors.append("display_name must be 50 characters or less")
    
    # Validate version
    if not validate_version(version):
        errors.append("version must follow SemVer 2.0.0 format (e.g., 1.0.0)")
    
    # Validate description
    if len(description) > 200:
        errors.append("description must be 200 characters or less")
    
    # Validate author_name
    if not author_name:
        errors.append("author_name is required")
    
    # Validate author_email
    if not validate_email(author_email):
        errors.append("author_email must be valid email format or empty")
    
    # Validate author_url
    if not validate_url(author_url):
        errors.append("author_url must be valid HTTP/HTTPS URL or empty")
    
    # Validate unity_version
    if not unity_version:
        errors.append("unity_version is required")
    elif not validate_unity_version(unity_version):
        errors.append("unity_version must be in YYYY.M format (e.g., 2022.3) or MAJOR.MINOR for Unity 6+")
    
    # Validate repo_url
    if repo_url and not validate_github_url(repo_url):
        errors.append("repo_url must be valid GitHub repository URL")
    
    # Exit with errors if validation failed
    if errors:
        print("Validation errors:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)
    
    print("Validation passed!")

if __name__ == "__main__":
    main()
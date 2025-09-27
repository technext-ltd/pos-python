# android_fix.py - Add this file to your repository
import os
import sys
from kivy.logger import Logger

def android_fix():
    """Apply Android-specific fixes"""
    try:
        # Check if we're running on Android
        if 'ANDROID_ARGUMENT' in os.environ:
            Logger.info('AndroidFix: Running on Android, applying fixes...')
            
            # Add Android-specific imports
            try:
                from android.permissions import request_permissions, Permission
                request_permissions([
                    Permission.WRITE_EXTERNAL_STORAGE,
                    Permission.READ_EXTERNAL_STORAGE,
                    Permission.INTERNET
                ])
                Logger.info('AndroidFix: Permissions requested')
            except ImportError:
                Logger.warning('AndroidFix: Could not request permissions')
                
            # Set up Android storage paths
            try:
                from android.storage import app_storage_path, primary_external_storage_path
                app_storage = app_storage_path()
                Logger.info(f'AndroidFix: App storage path: {app_storage}')
            except ImportError:
                Logger.warning('AndroidFix: Could not get Android storage paths')
                
    except Exception as e:
        Logger.error(f'AndroidFix: Error applying fixes: {e}')

def get_android_storage_path():
    """Get appropriate storage path for Android"""
    try:
        if 'ANDROID_ARGUMENT' in os.environ:
            from android.storage import app_storage_path
            storage_path = app_storage_path()
            # Create data directory if it doesn't exist
            data_dir = os.path.join(storage_path, 'pos_data')
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)
            return data_dir
        else:
            # On PC, use current directory
            return os.path.dirname(os.path.abspath(__file__))
    except Exception as e:
        Logger.error(f'AndroidFix: Error getting storage path: {e}')
        return os.path.dirname(os.path.abspath(__file__))

from kivy.logger import Logger
Logger.info("[INFO CC]")
Logger.warning("[WARNING CC]")
Logger.error("[ERROR CC]")

try:
    from setuptools_rust import RustExtension
    Logger.info("[CC LOG] setuptools_rust library imported successfully!")
except Exception as e:
	Logger.error(f"[CC LOG] setuptools_rust library import failed: {e}", exc_info=True)
	

try:
	from kivy.app import App
	from kivy.graphics import Color, Line, Rectangle, RoundedRectangle, Ellipse
	from kivy.uix.widget import Widget
	from kivy.uix.boxlayout import BoxLayout
	from kivy.uix.floatlayout import FloatLayout
	from kivy.uix.gridlayout import GridLayout
	from kivy.core.text import Label as CoreLabel
	from kivy.uix.label import Label, CoreLabel
	from kivy.uix.button import Button
	from kivy.uix.image import Image
	from kivy.uix.togglebutton import ToggleButton
	from kivy.uix.behaviors import ToggleButtonBehavior
	from kivy.uix.textinput import TextInput
	from kivy.uix.checkbox import CheckBox
	from kivy.uix.spinner import Spinner
	from kivy.uix.slider import Slider
	from kivy.uix.scrollview import ScrollView
	from kivy.animation import Animation
	from kivy.clock import Clock
	from kivy.utils import platform
	
	Logger.info("[CC LOG] Kivy libraries imported successfully!")

except Exception as e:
	Logger.error(f"[CC LOG] Kivy libraries import failed: {e}", exc_info=True)	


try:
	import ctypes, sys
	if platform != "macosx":
		ctypes.pythonapi = ctypes.PyDLL("libpython%d.%d.so" % sys.version_info[:2])   # replaces ctypes.PyDLL(None)
	Logger.info("[CC LOG] ctypes and sys libraries imported successfully!")
except Exception as e:
	Logger.error(f"[CC LOG] ctypes or sys import failed (dsiabled error message)", exc_info=True)	


try:
	import Crypto
	Logger.info("[CC LOG] Crypto library imported successfully!")
except Exception as e:
	Logger.error(f"[CC LOG] Crypto library import failed: {e}", exc_info=True)


try:
	import cryptography
	from cryptography.hazmat.primitives import serialization
	from cryptography.hazmat.primitives.asymmetric import rsa
	from cryptography.hazmat.primitives.asymmetric import padding
	from cryptography.hazmat.primitives import hashes
	from cryptography.hazmat.backends import default_backend # NEW
	from cryptography.x509 import load_pem_x509_certificate
	import base64
	Logger.info("[CC LOG] cryptography and base64 library imported successfully!")
except Exception as e:
	Logger.error(f"[CC LOG] cryptography library import failed: {e}", exc_info=True)


try:
	import sqlite3
	Logger.info("[CC LOG] sqlite3 library imported successfully!")
except Exception as e:
	Logger.error(f"[CC LOG] sqlite3 library import failed: {e}", exc_info=True)


try:
	import json
	Logger.info("[CC LOG] json library imported successfully!")
except Exception as e:
	Logger.error(f"[CC LOG] json library import failed: {e}", exc_info=True)	


try:
	import requests
	Logger.info("[CC LOG] requests library imported successfully!")
except Exception as e:
	Logger.error(f"[CC LOG] requests library import failed: {e}", exc_info=True)


try:
	import pyrebase
	Logger.info("[CC LOG] pyrebase library imported successfully!")
except Exception as e:
	Logger.error(f"[CC LOG] pyrebase library import failed: {e}", exc_info=True)


try:
	import urllib.request
	import urllib.error
	import ssl
	Logger.info("[CC LOG] urllib and ssl library imported successfully!")
except Exception as e:
	Logger.error(f"[CC LOG] urllib or ssl library import failed: {e}", exc_info=True)

	
try:
	import random
	import time
	from time import time as get_current_time
	from datetime import datetime, timedelta
	from topics import all_topics
	
	Logger.info("[CC LOG] Remaining libraries imported successfully!")

except Exception as e:
	Logger.error(f"[CC LOG] One of the remaining libraries imports failed: {e}", exc_info=True)



try:
	FIREBASE_KEY = "AIzaSyAnBhItqbtgF0R7_6Kfaqhi_N2Nh43XyV0"
	FIREBASE_PROJECT_ID = "convokeeper-project"
	firebase_config = {
		"apiKey": FIREBASE_KEY,
		"authDomain": f"{FIREBASE_PROJECT_ID}.firebaseapp.com",
		"databaseURL": f"https://{FIREBASE_PROJECT_ID}-default-rtdb.firebaseio.com",
		"storageBucket": f"{FIREBASE_PROJECT_ID}.appspot.com"
	}
	
	Logger.info("[CC LOG] Firebase varialbes set successfully!")

except Exception as e:
	Logger.error(f"[CC LOG] Failed to set Firebase variables: {e}", exc_info=True)


try:
	# Global configuration for CustomBoxLayout class
	GLOBAL_BOX_BACKGROUND_COLOR = (0.15, 0.16, 0.18, 1) # (0.15, 0.16, 0.18, 1)
	GLOBAL_BOX_LINE_COLOR = (0, 0, 0, 0) # Turquoise (0, 1, 1, 1)
	GLOBAL_BOX_LINE_WIDTH = 1

	# Global configuration for CustomFloatLayout class
	GLOBAL_FLOAT_BACKGROUND_COLOR = (0, 0, 0, 0)
	GLOBAL_FLOAT_LINE_COLOR = (0, 0, 0, 0) # Yellow (1, 1, 0, 1)
	GLOBAL_FLOAT_LINE_WIDTH = 1

	# Global configuration for CustomGridLayout class
	GLOBAL_GRID_BACKGROUND_COLOR = (0, 0, 0, 0)
	GLOBAL_GRID_LINE_COLOR = (0, 0, 0, 0) # Pink (1, 0, 1, 1)
	GLOBAL_GRID_LINE_WIDTH = 1

	# Global configuration for CustomButton class
	GLOBAL_BUTTON_BACKGROUND_COLOR_NORMAL = (0, 0, 0, 0)
	GLOBAL_BUTTON_BACKGROUND_COLOR_FLICKER = (0, 0, 0, 0.3)
	GLOBAL_BUTTON_LINE_COLOR = (0, 0, 0, 0) # White (1, 1, 1, 1)
	GLOBAL_BUTTON_LINE_WIDTH = 1
	GLOBAL_BUTTON_TYPE = 'Normal'

	# Global configuration for CustomLabel class
	GLOBAL_LABEL_BACKGROUND_COLOR = (0, 0, 0, 0)
	GLOBAL_LABEL_LINE_COLOR = (0, 0, 0, 0) # Gray (0.5, 0.5, 0.5, 0.5)
	GLOBAL_LABEL_LINE_WIDTH = 1

	# Global configuration for ModalOverlay class
	GLOBAL_OVERLAY_BACKGROUND_COLOR = (1, 1, 0, 1)
	GLOBAL_OVERLAY_LINE_COLOR = (0, 0, 0, 0) # Red (1, 0, 0, 1)
	GLOBAL_OVERLAY_LINE_WIDTH = 1

	# Global configuration for CustomTextInput class
	GLOBAL_INPUT_BACKGROUND_COLOR = (1, 1, 1, 0.1)
	GLOBAL_INPUT_LINE_COLOR = (0, 0, 0, 0)
	GLOBAL_INPUT_LINE_WIDTH = 1
	GLOBAL_INPUT_HINT_TEXT_COLOR = (0.83, 0.84, 0.85, 1)
	GLOBAL_INPUT_FOREGROUND_TEXT_COLOR = (1, 1, 1, 1)

	# GLobal configuration for fonts
	GLOBAL_FONT_COLOR = (1, 1, 1, 1)
	GLOBAL_FONT_SIZE = 34
	GLOBAL_FONT_NAME = "fonts/AfacadFlux-Regular"
	GLOBAL_FONT_BOLD = "fonts/AfacadFlux-SemiBold"
	GLOBAL_FONT_UNICODE = "fonts/fa-solid-900"

	# Global configuration for shapes
	GLOBAL_SHAPE_TYPE = "rectangle_rounded"
	GLOBAL_CORNER_RADIUS = 20
	Logger.info("[CC LOG] All global variables set successfully!")

except Exception as e:
	Logger.error(f"[CC LOG] Failed to set global variables: {e}", exc_info=True)


try:
	class ModalOverlay(Widget):
		def __init__(self, 
					 app_ref, 
					 background_color=GLOBAL_OVERLAY_BACKGROUND_COLOR, 
					 line_color=GLOBAL_OVERLAY_LINE_COLOR, 
					 line_width=GLOBAL_OVERLAY_LINE_WIDTH, 
					 **kwargs):
		
			super(ModalOverlay, self).__init__(**kwargs)
		
			# Set values for the parameters
			self.app_ref = app_ref    # Store a reference to the ConvoKeeper class object
			self.background_color = background_color
			self.line_color = line_color
			self.line_width = line_width
		
			# Drawing the rectangle using canvas instructions
			with self.canvas.before:
			
				# Set the background color
				Color(*self.background_color)
			
				# Draw rectangle
				self.rect = Rectangle(pos=self.pos, size=self.size)
			
				# Set the line color
				Color(*self.line_color) # Affects next drawing instruction, in this case Line 
			
				# Draw the line with or without rounded corners
				self.border_line = Line(rectangle=self.pos + self.size, width=self.line_width)
		
			# Bind the size and position to always cover the window
			self.bind(pos=self.update_graphics, size=self.update_graphics)
	
		"""Update the rectangle size and position to cover the window."""
		def update_graphics(self, *args):
			self.rect.pos = self.pos
			self.rect.size = self.size
			self.border_line.rectangle = self.pos + self.size



	class CustomFloatLayout(FloatLayout):
		def __init__(self, 
					 background_color=GLOBAL_FLOAT_BACKGROUND_COLOR, 
					 line_color=GLOBAL_FLOAT_LINE_COLOR, 
					 line_width=GLOBAL_FLOAT_LINE_WIDTH, 
					 shape_type=GLOBAL_SHAPE_TYPE, 
					 corner_radius=GLOBAL_CORNER_RADIUS, 
					 **kwargs):
		
			super(CustomFloatLayout, self).__init__(**kwargs)
		
			# Set values for the parameters:
			self.background_color = background_color
			self.line_color = line_color
			self.line_width = line_width
			self.shape_type = shape_type
			self.corner_radius = corner_radius

			# Drawing the background and line using canvas instructions
			with self.canvas.before:
			
				# Set the background color
				Color(*self.background_color) # Affects next drawing instruction, in this case Rectangle
			
				# Draw rectangle with or without rounded corners
				if(self.shape_type == "rectangle_rounded"):
					self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[self.corner_radius])
				else:
					self.rect = Rectangle(pos=self.pos, size=self.size)

				# Set the line color
				Color(*self.line_color) # Affects next drawing instruction, in this case Line
			
				# Draw the line with or without rounded corners
				if(self.shape_type == "rectangle_rounded"):
					self.line = Line(rounded_rectangle=(self.pos[0], self.pos[1], self.size[0], self.size[1], self.corner_radius), width=self.line_width)
				elif(self.shape_type == "rectangle"):
					self.line = Line(rectangle=self.pos + self.size, width=self.line_width)
				elif(self.shape_type == "line_right"):
					self.line = Line(points=[self.pos[0] + self.size[0], self.pos[1] + self.size[1], self.pos[0] + self.size[0], self.pos[1]], width=self.line_width)

			# Bind position and size updates to adjust the background and line
			self.bind(pos=self.update_graphics, size=self.update_graphics)

		def update_graphics(self, *args):
		
			#if self.shape_type == "line_right":
				 #print(f"PARENT.size.before:      {self.size}")
		
			# Update the background and line when the layout changes size or position
			self.rect.pos = self.pos
			self.rect.size = self.size
		
			if(self.shape_type == "rectangle_rounded"):
				self.line.rounded_rectangle = (*self.pos, *self.size, self.corner_radius)
			elif(self.shape_type == "rectangle"):
				self.line.rectangle = (*self.pos, *self.size)
			elif(self.shape_type == "line_right"):
				self.line.points = [self.pos[0] + self.size[0], self.pos[1] + self.size[1], self.pos[0] + self.size[0], self.pos[1]]

			#if self.shape_type == "line_right":
				 #print(f"PARENT.size.after:       {self.size}")



	class CustomBoxLayout(BoxLayout):
		def __init__(self, 
					 app_ref=None, 
					 background_color=GLOBAL_BOX_BACKGROUND_COLOR, 
					 line_color=GLOBAL_BOX_LINE_COLOR, 
					 line_width=GLOBAL_BOX_LINE_WIDTH, 
					 shape_type=GLOBAL_SHAPE_TYPE, 
					 corner_radius=GLOBAL_CORNER_RADIUS, 
					 **kwargs):
		
			super(CustomBoxLayout, self).__init__(**kwargs)
		
			# Set values for the parameters
			self.app_ref = app_ref
			self.background_color = background_color
			self.line_color = line_color
			self.line_width = line_width
			self.shape_type = shape_type
			self.corner_radius = corner_radius

			# Drawing the background and line using canvas instructions
			with self.canvas.before:
			
				# Set the background color
				Color(*self.background_color) # Affects next drawing instruction, in this case Rectangle
			
				# Draw rectangle with or without rounded corners
				if(self.shape_type == "rectangle_rounded"):
					self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[self.corner_radius])
				else:
					self.rect = Rectangle(pos=self.pos, size=self.size)

				# Set the line color
				Color(*self.line_color) # Affects next drawing instruction, in this case Line
			
				# Draw the line with or without rounded corners
				if(self.shape_type == "rectangle_rounded"):
					self.line = Line(rounded_rectangle=(self.pos[0], self.pos[1], self.size[0], self.size[1], self.corner_radius), width=self.line_width)
				elif(self.shape_type == "rectangle"):
					self.line = Line(rectangle=self.pos + self.size, width=self.line_width)
				elif(self.shape_type == "line_top"):
					self.line = Line(points=[self.pos[0], self.pos[1] + self.size[1], self.pos[0] + self.size[0], self.pos[1] + self.size[1]], width=self.line_width)
				elif(self.shape_type == "line_bottom"):
					self.line = Line(points=[self.pos[0], self.pos[1], self.pos[0] + self.size[0], self.pos[1]], width=self.line_width)
				elif(self.shape_type == "line_left"):
					self.line = Line(points=[self.pos[0], self.pos[1] + self.size[1], self.pos[0], self.pos[1]], width=self.line_width)
				elif(self.shape_type == "line_right"):
					self.line = Line(points=[self.pos[0] + self.size[0], self.pos[1] + self.size[1], self.pos[0] + self.size[0], self.pos[1]], width=self.line_width)

			# Bind position and size updates to adjust the background and line
			self.bind(pos=self.update_graphics, size=self.update_graphics)

		def update_graphics(self, *args):  	
		
			self.rect.pos = self.pos
			self.rect.size = self.size
		
			if(self.shape_type == "rectangle_rounded"):
				self.line.rounded_rectangle = (*self.pos, *self.size, self.corner_radius)
			elif(self.shape_type == "rectangle"):
				self.line.rectangle = (*self.pos, *self.size)
			elif(self.shape_type == "line_top"):
				self.line.points = [self.pos[0], self.pos[1] + self.size[1], self.pos[0] + self.size[0], self.pos[1] + self.size[1]]
			elif(self.shape_type == "line_bottom"):
				self.line.points = [self.pos[0], self.pos[1], self.pos[0] + self.size[0], self.pos[1]]
			elif(self.shape_type == "line_left"):
				self.line.points = [self.pos[0], self.pos[1] + self.size[1], self.pos[0], self.pos[1]]
			elif(self.shape_type == "line_right"):
				self.line.points = [self.pos[0] + self.size[0], self.pos[1] + self.size[1], self.pos[0] + self.size[0], self.pos[1]] 



	class CustomGridLayout(GridLayout):
		def __init__(self, 
					 background_color=GLOBAL_GRID_BACKGROUND_COLOR, 
					 line_color=GLOBAL_GRID_LINE_COLOR, 
					 line_width=GLOBAL_GRID_LINE_WIDTH, 
					 shape_type=GLOBAL_SHAPE_TYPE, 
					 corner_radius=GLOBAL_CORNER_RADIUS, 
					 **kwargs):
		
			super(CustomGridLayout, self).__init__(**kwargs)
		
			# Set values for the parameters
			self.background_color = background_color
			self.line_color = line_color
			self.line_width = line_width
			self.shape_type = shape_type
			self.corner_radius = corner_radius

			# Drawing the background and line using canvas instructions
			with self.canvas.before:
			
				# Set the background color
				Color(*self.background_color) # Affects next drawing instruction, in this case Rectangle
			
				# Draw rectangle with or without rounded corners
				if(self.shape_type == "rectangle_rounded"):
					self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[self.corner_radius])
				else:
					self.rect = Rectangle(pos=self.pos, size=self.size)

				# Set the line color
				Color(*self.line_color) # Affects next drawing instruction, in this case Line
			
				# Draw the line with or without rounded corners
				if(self.shape_type == "rectangle_rounded"):
					self.line = Line(rounded_rectangle=(self.pos[0], self.pos[1], self.size[0], self.size[1], self.corner_radius), width=self.line_width)
				elif(self.shape_type == "rectangle"):
					self.line = Line(rectangle=self.pos + self.size, width=self.line_width)

			# Bind position and size updates to adjust the background and line
			self.bind(pos=self.update_graphics, size=self.update_graphics)

		def update_graphics(self, *args):
		
			# Update the background and line when the layout changes size or position
			self.rect.pos = self.pos
			self.rect.size = self.size
		
			if(self.shape_type == "rectangle_rounded"):
				self.line.rounded_rectangle = (*self.pos, *self.size, self.corner_radius)
			elif(self.shape_type == "rectangle"):
				self.line.rectangle = (*self.pos, *self.size)
			elif(self.shape_type == "line_right"):
				self.line.points = [self.pos[0] + self.size[0], self.pos[1] + self.size[1], self.pos[0] + self.size[0], self.pos[1]]



	class CustomLabel(Label):
		def __init__(self, 
					 app_ref=None,
					 font_size_previous=0,
					 previous_width=100,
					 previous_height=100,
					 label_type="Standard", 
					 background_color=GLOBAL_LABEL_BACKGROUND_COLOR, 
					 line_color=GLOBAL_LABEL_LINE_COLOR, 
					 line_width=GLOBAL_LABEL_LINE_WIDTH, 
					 shape_type=GLOBAL_SHAPE_TYPE, 
					 corner_radius=GLOBAL_CORNER_RADIUS, 
					 **kwargs):
		
			super(CustomLabel, self).__init__(**kwargs)
		
			# Set values for the parameters
			self.app_ref = app_ref
			self.markup = True
			self.font_size_previous = font_size_previous
			self.previous_width = previous_width
			self.previous_height = previous_height
			self.label_type = label_type
			self.disabled_color = self.color # Prevents Kivy prom settings its default text color when a widget is disabled
			self.background_color = background_color
			self.line_color = line_color
			self.line_width = line_width
			self.shape_type = shape_type
			self.corner_radius = corner_radius
			self.font_name = kwargs.get('font_name', GLOBAL_FONT_NAME)
			self.font_size = kwargs.get('font_size', GLOBAL_FONT_SIZE)
			self.font_size_initial = self.font_size
			self.color = kwargs.get('color', GLOBAL_FONT_COLOR)
		
			# Initial text alignment
			self.text_size = (self.width, self.height)  # Allow wrapping based on the width
			self.halign = kwargs.get('halign', 'center')  # Horizontal alignment of text
			self.valign = kwargs.get('valign', 'middle')  # Vertical alignment of text
			self.bind(size=self.update_text_size)
		
			# Drawing the background and line using canvas instructions
			with self.canvas.before:
				# Set the background color
				self.shape_bg_color = Color(*self.background_color)  # Affects next drawing instruction, in this case Rectangle
			
				# Draw rectangle with or without rounded corners
				if(self.shape_type == "rectangle_rounded"):
					self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[self.corner_radius])
				else:
					self.rect = Rectangle(pos=self.pos, size=self.size)

				# Set the line color
				self.line_bg_color = Color(*self.line_color) # Affects next drawing instruction, in this case Line
			
				# Draw the line with or without rounded corners
				if(self.shape_type == "rectangle_rounded"):
					self.line = Line(rounded_rectangle=(self.pos[0], self.pos[1], self.size[0], self.size[1], self.corner_radius), width=self.line_width)
				else:
					self.line = Line(rectangle=self.pos + self.size, width=self.line_width)
		
			# Bind position and size updates to adjust the background and line
			self.bind(pos=self.update_graphics, size=self.update_graphics)

		"""Update the text size to match the label size for wrapping."""
		def update_text_size(self, *args):
			self.text_size = (self.width, self.height)  # Wrap text based on the current label width

		"""Update the background and line when the layout changes size or position."""
		def update_graphics(self, *args):
			# Dynamically resize font when button changes height or width
			if isinstance(self.parent, CustomButton):
				instance = self.parent
				# self.parent.app_ref.dynamically_set_font_size(instance)
			else:
				instance = self
				# self.app_ref.dynamically_set_font_size(instance)
		
			# Re-position and resize rectangle/shape to match widget position and size
			self.rect.pos = self.pos
			self.rect.size = self.size
			
			# Adjust size of favorites list and each item in it
			if self.label_type == "Favorite category" and self.children != None:
				box_height = self.app_ref.widget_parent_body_CBL.height - (self.app_ref.widget_label_favorites_CL.height)
				favorite_category_label_height = 70
				favorite_catgoriy_labels_total_height = favorite_category_label_height * self.app_ref.favorite_categories_count
			
				if favorite_catgoriy_labels_total_height >= box_height:
					favorite_category_label_height = box_height / self.app_ref.favorite_categories_count
			
				self.parent.height = (self.app_ref.favorite_categories_count * favorite_category_label_height) + (self.app_ref.favorite_categories_count * self.parent.spacing)
				self.height = favorite_category_label_height
			
				for child in self.children:
					child.width = favorite_category_label_height
					child.height = favorite_category_label_height
					if child.text == "\uF1F8":
						child.x = self.pos[0]
						child.y = self.center_y - child.height/2
					else:
						child.x = self.pos[0] + self.size[0] - child.width
						child.y = self.center_y - child.height/2
		
			# Re-draw the line for the shape
			if(self.shape_type == "rectangle_rounded"):
				self.line.rounded_rectangle = (*self.pos, *self.size, self.corner_radius)
			else:
				self.line.rectangle = (*self.pos, *self.size)



	class CustomButton(Button):
	
		currently_pressed_button = None # Initialize the most recently pressed button
		previously_pressed_button = None
		last_pressed_category_button = None
		last_pressed_menu_button = None
	
		def __init__(self, 
					 app_ref=None,
					 font_size_previous=0,
					 previous_width=100,
					 previous_height=100,
					 background_color_normal=GLOBAL_BUTTON_BACKGROUND_COLOR_NORMAL, 
					 background_color_flicker=GLOBAL_BUTTON_BACKGROUND_COLOR_FLICKER, 
					 background_color_selected=None, 
					 line_color=GLOBAL_BUTTON_LINE_COLOR, 
					 line_width=GLOBAL_BUTTON_LINE_WIDTH, 
					 shape_type=GLOBAL_SHAPE_TYPE, 
					 corner_radius=GLOBAL_CORNER_RADIUS, 
					 button_type=GLOBAL_BUTTON_TYPE, 
					 **kwargs):
			super(CustomButton, self).__init__(**kwargs)
		
			# Set values for the parameters
			self.app_ref = app_ref  # Store a reference to the ConvoKeeper class object
			self.markup = True
			self.is_favorite = False
			self.font_size_previous = font_size_previous
			self.initial_size = [0, 0]
			self.previous_width = previous_width
			self.previous_height = previous_height
			self.background_normal = ''  # Disable the default background image (i.e. the dark gray tint)
			self.background_down = ''  # Disable the background when the button is pressed
			self.background_color = (0, 0, 0, 0)  # Set the default background to transparent
			self.disabled_color = self.color # Prevents Kivy from settings its default text color when a widget is disabled
			self.line_color = line_color
			self.line_width = line_width
			self.shape_type = shape_type
			self.corner_radius = corner_radius
			self.font_name = kwargs.get('font_name', GLOBAL_FONT_NAME)
			self.font_size = kwargs.get('font_size', GLOBAL_FONT_SIZE)
			self.font_size_initial = self.font_size
			self.color = kwargs.get('color', GLOBAL_FONT_COLOR)
			self.button_type = button_type
			self.background_color_normal = kwargs.get('background_color', background_color_normal) # Looks for 'background_color' in kwargs and if not found uses background_color_normal as fallback
			self.background_color_flicker = background_color_flicker
			self.background_color_selected = (
				background_color_selected  # Check for background_color_selected
				or kwargs.get('background_color')  # Fallback to background_color from kwargs
				or background_color_normal  # Fallback to background_color_normal if neither is set
			)
		
			# Initial text alignment
			self.halign = kwargs.get('halign', 'center')  # Horizontal alignment of text
			self.valign = kwargs.get('valign', 'middle')  # Vertical alignment of text
			self.text_size = (self.width, self.height)  # Text size = Size of the text box --> Allow wrapping based on the width
			self.bind(size=self.update_text_size)
		
			# Add label inside the category button containing the favorite icon (only runs during initial build)
			if self.button_type == 'Category':
				self.widget_favorite_label = CustomLabel(app_ref=self, text="uf006", size_hint=(None, None), size=(40, 40), color=(0.97, 0.53, 0.20, 1), font_name="fonts/fa-regular-400", font_size=36, shape_type="rectangle", halign="center")
				self.add_widget(self.widget_favorite_label)
				self.widget_favorite_label.bind(on_touch_down=self.app_ref.favorite_icon_pressed)
		
			# Drawing the background and line using canvas instructions
			with self.canvas.before:
			
				# Set the background color
				self.shape_bg_color = Color(*self.background_color_normal)
			
				# Draw rectangle with or without rounded corners
				if(self.shape_type == "rectangle_rounded"):
					self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[self.corner_radius])
				else:
					self.rect = Rectangle(pos=self.pos, size=self.text_size)
			
				# Set the line color
				self.line_bg_color = Color(*self.line_color) # Affects next drawing instruction, in this case Line 
			
				# Draw the line with or without rounded corners
				if(self.shape_type == "rectangle_rounded"):
					self.line = Line(rounded_rectangle=(self.pos[0], self.pos[1], self.size[0], self.size[1], self.corner_radius), width=self.line_width)
				elif(self.shape_type == "rectangle"):
					self.line = Line(rectangle=self.pos + self.size, width=self.line_width)
				elif(self.shape_type == "line_menu"):
					#self.line_bottom = Line(points=[self.pos[0], self.pos[1], self.pos[0] + self.size[0] - self.corner_radius, self.pos[1]], width=self.line_width)
					#self.line_right = Line(points=[self.pos[0] + self.size[0], self.pos[1] + self.corner_radius, self.pos[0] + self.size[0], self.pos[1] + self.size[1] - self.corner_radius], width=self.line_width)
					#self.line_corner_br = Line(circle=(self.pos[0] + self.size[0] - self.corner_radius, self.pos[1] + self.corner_radius, self.corner_radius, 90, 180), width=self.line_width)     
					self.line_corner_tl_hor = Line(points=[self.pos[0], self.pos[1] + self.height - 3, self.pos[0] + 12, self.pos[1] + self.height - 3], width=self.line_width)
					self.line_corner_tl_ver = Line(points=[self.pos[0], self.pos[1] + self.height - 3, self.pos[0], self.pos[1] + self.height - 12 - 3], width=self.line_width)
					self.line_corner_br_hor = Line(points=[self.pos[0] + self.width, self.pos[1], self.pos[0] + self.width - 12, self.pos[1]], width=self.line_width)
					self.line_corner_br_ver = Line(points=[self.pos[0] + self.width, self.pos[1], self.pos[0] + self.width, self.pos[1] + 12], width=self.line_width)
		
			# Bind position and size to update the rounded rectangle
			self.bind(pos=self.update_graphics, size=self.update_graphics)
	
		"""Update the text size to match the button size for wrapping."""
		def update_text_size(self, *args):
			self.text_size = (self.width, self.height)  # Wrap text based on the current button width

		"""Update the background and line when the button changes size or position."""
		def update_graphics(self, *args):
			# Dynamically resize font when button changes height or width
			# self.app_ref.dynamically_set_font_size(self)
		
			# Re-position and resize rectangle/shape to match widget position and size
			self.rect.pos = self.pos
			self.rect.size = self.size
		
			# Position the favorite category icon
			if self.button_type == 'Category':
				self.widget_favorite_label.pos = (self.right - 50, self.top - 50)
		
			# Re-draw the line for the shape
			if(self.shape_type == "rectangle_rounded"):
				self.line.rounded_rectangle = (*self.pos, *self.size, self.corner_radius)
			elif(self.shape_type == "rectangle"):
				self.line.rectangle = (*self.pos, *self.size)
			elif(self.shape_type == "line_menu"):
				label = CoreLabel(text=self.text, font_size=self.font_size, font_name=self.font_name)
				label.refresh()  # Render the text to calculate texture size
				text_width = label.texture.size[0]
				text_height = label.texture.size[1]
				self.line_corner_tl_hor.points = [self.pos[0] - 6, self.pos[1] + text_height - 4, self.pos[0] + 6, self.pos[1] + text_height - 4]
				self.line_corner_tl_ver.points = [self.pos[0] - 6, self.pos[1] + text_height - 4, self.pos[0] - 6, self.pos[1] + text_height - 4 - 12]
				self.line_corner_br_hor.points = [self.pos[0] + text_width + 7, self.pos[1] + 2, self.pos[0] + text_width - 7, self.pos[1] + 2]
				self.line_corner_br_ver.points = [self.pos[0] + text_width + 7, self.pos[1] + 2, self.pos[0] + text_width + 7, self.pos[1] + 2 + 12]
				
		"""Background color when the button is pressed."""
		def on_press(self):
			self.shape_bg_color.rgba = self.background_color_flicker
	
		"""Background color when the button is released."""
		def on_release(self):
		
			CustomButton.previously_pressed_button = CustomButton.currently_pressed_button # currently_pressed_button has not yet been updated to the most recently pressed button
			CustomButton.currently_pressed_button = self # Here currently_pressed_button gets updated to the most recently pressed button
			CustomButton.last_pressed_category_button = CustomButton.last_pressed_category_button
			CustomButton.last_pressed_menu_button = CustomButton.last_pressed_menu_button
		
			if CustomButton.currently_pressed_button != None and CustomButton.currently_pressed_button == self:
				# print("A custom button has been pressed and set to the currently pressed button")
			
				if CustomButton.currently_pressed_button.button_type != 'Category' and CustomButton.currently_pressed_button.button_type != 'Menu':
					if self.app_ref: # Checks that there is a reference to the ConvoKeeper class/object
						self.app_ref.apply_layout_for_standard_buttons()
			
				elif CustomButton.currently_pressed_button.button_type == 'Category':
					if self.app_ref: # Checks that there is a reference to the ConvoKeeper class/object
						self.app_ref.apply_layout_for_category_buttons()
			
				elif CustomButton.currently_pressed_button.button_type == 'Menu':
					if self.app_ref: # Checks that there is a reference to the ConvoKeeper class/object
						self.app_ref.apply_layout_for_menu_buttons()
	
	
	
	class CustomToggleButton(ToggleButton):
		def __init__(self, 
					 app_ref=None,
					 toggle_name="", 
					 **kwargs):
			super(CustomToggleButton, self).__init__(**kwargs)
		
			# Set the button properties
			self.app_ref = app_ref  # Store a reference to the ConvoKeeper class object
			self.toggle_name = toggle_name
			self.background_normal = ''  # No default background
			self.background_color = (0, 0, 0, 0)  # Transparent background
		
			# Create color instructions for the background
			with self.canvas.before:
			
				# Background color
				self.bg_color = Color(0.2, 0.8, 0.2, 1)  # Default color
				self.rect_bg = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])
			
				# Circle for the toggle switch
				self.circle_color = Color(1, 1, 1, 1)  # White color for the toggle circle
				self.toggle_circle = RoundedRectangle(size=(self.height, self.height), pos=(self.x, self.y), radius=[20])
			
				self.bind(pos=self.update_graphics, size=self.update_graphics)
			self.bind(state=self.on_state)  # Bind state to change colors

		def update_graphics(self, *args):
			self.rect_bg.pos = self.pos
			self.rect_bg.size = self.size
			self.rect_bg.radius = [self.height/2]

			# Position the toggle circle
			if self.state == 'normal':
				self.toggle_circle.pos = (self.x + self.width - self.height, self.y)  # Move to the right
			else:
				self.toggle_circle.pos = (self.x, self.y)  # Move to the left

			# Update the size of the circle
			self.toggle_circle.size = (self.height, self.height)
			self.toggle_circle.radius = [self.height/2]

		def on_state(self, widget, value):
			if value == 'normal':
				Animation(pos=(self.x + self.width - self.height, self.y), duration=0.2).start(self.toggle_circle)
				self.bg_color.rgba = (0.2, 0.8, 0.2, 1)  # Color when pressed
			else:
				Animation(pos=(self.x, self.y), duration=0.2).start(self.toggle_circle)
				self.bg_color.rgba = (0.6, 0.6, 0.6, 1)  # Color when not pressed
	
	
	
	class CustomTextInput(TextInput):
		def __init__(self, 
					 app_ref=None,
					 font_size_previous=0,
					 previous_width=100,
					 previous_height=100,
					 bg_color=GLOBAL_INPUT_BACKGROUND_COLOR, 
					 line_color=GLOBAL_INPUT_LINE_COLOR, 
					 line_width=GLOBAL_INPUT_LINE_WIDTH, 
					 shape_type=GLOBAL_SHAPE_TYPE, 
					 corner_radius=GLOBAL_CORNER_RADIUS, 
					 **kwargs):
		
			super(CustomTextInput, self).__init__(**kwargs)
		
			# Set values for the parameters
			self.app_ref = app_ref
			self.markup = True
			self.font_size_previous = font_size_previous
			self.previous_width = previous_width
			self.previous_height = previous_height
			self.background_normal = ""
			self.background_active = ""
			self.background_color = [0, 0, 0, 0]
			self.border = [0, 0, 0, 0]
			self.bg_color = bg_color
			self.disabled_color = self.hint_text_color # Prevents Kivy from setting its default text color when a widget is disabled
			self.line_color = line_color
			self.line_width = line_width
			self.shape_type = shape_type
			self.corner_radius = corner_radius
			self.font_name = kwargs.get('font_name', GLOBAL_FONT_NAME)
			self.font_size = kwargs.get('font_size', GLOBAL_FONT_SIZE)
			self.font_size_initial = self.font_size
			self.hint_text_color = kwargs.get('hint_text_color', GLOBAL_INPUT_HINT_TEXT_COLOR)
			self.foreground_color = kwargs.get('foreground_color', GLOBAL_INPUT_FOREGROUND_TEXT_COLOR)
		
			# Initial text alignment
			self.text_size = (self.width, self.height)  # Allow wrapping based on the width
			self.halign = kwargs.get('halign', 'center')  # Horizontal alignment of text
			self.valign = kwargs.get('valign', 'middle')  # Vertical alignment of text
			self.bind(size=self.update_text_size)
		
		
			# Drawing the background and line using canvas instructions
			with self.canvas.after:
				# Set the background color
				self.shape_bg_color = Color(*self.bg_color)  # Affects next drawing instruction, in this case Rectangle
			
				# Draw rectangle with or without rounded corners
				if(self.shape_type == "rectangle_rounded"):
					self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[self.corner_radius])
				else:
					self.rect = Rectangle(pos=self.pos, size=self.size)

				# Set the line color
				self.line_bg_color = Color(*self.line_color) # Affects next drawing instruction, in this case Line
			
				# Draw the line with or without rounded corners
				if(self.shape_type == "rectangle_rounded"):
					self.line = Line(rounded_rectangle=(self.pos[0], self.pos[1], self.size[0], self.size[1], self.corner_radius), width=self.line_width)
				else:
					self.line = Line(rectangle=self.pos + self.size, width=self.line_width)
		
			# Bind position and size updates to adjust the background and line
			self.bind(pos=self.update_graphics, size=self.update_graphics)

		"""Update the text size to match the label size for wrapping."""
		def update_text_size(self, *args):
			self.text_size = (self.width, self.height)  # Wrap text based on the current label width

		"""Update the background and line when the layout changes size or position."""
		def update_graphics(self, *args):
		
			#print("")
			#print(f"self.hint_text: {self.hint_text}")
			#print(f"self.font_size: {self.font_size}")
			#print(f"self:           {self}")
			#print(f"self.app_ref:   {self.app_ref}")
		
			# Dynamically resize font when button changes height or width
			# self.app_ref.dynamically_set_font_size(self)
		
			# Re-position and resize rectangle/shape to match widget position and size
			self.rect.pos = self.pos
			self.rect.size = self.size
		
			# Re-draw the line for the shape
			if(self.shape_type == "rectangle_rounded"):
				self.line.rounded_rectangle = (*self.pos, *self.size, self.corner_radius)
			else:
				self.line.rectangle = (*self.pos, *self.size)
	
	
	
	class SessionManager:
		"""Manages user session during the app's runtime."""
		def __init__(self):
			self.id_token = None  # Store the idToken here

		def set_id_token(self, id_token):
			self.id_token = id_token

		def get_id_token(self):
			return self.id_token

		def clear_session(self):
			self.id_token = None
	
	
	
	class TokenValidator:
		"""Handles local validation of Firebase ID tokens."""
		
		Logger.info("[CC LOG] Token validator class called")
		
		def __init__(self, firebase_project_id):
			self.firebase_project_id = firebase_project_id
			self.public_keys_url = "https://www.googleapis.com/robot/v1/metadata/x509/securetoken@system.gserviceaccount.com"
			self.public_keys = None
			Logger.info(f"[CC LOG] self.firebase_project_id: {self.firebase_project_id}")
			Logger.info(f"[CC LOG] self.public_keys_url: {self.public_keys_url}")

		def fetch_public_keys(self):
			"""Fetch Firebase's public keys for token verification."""
			try:
				response = requests.get(self.public_keys_url)
				if response.status_code == 200:
					self.public_keys = response.json()
					Logger.info(f"[CC LOG] Public keys fetched successfully: {self.public_keys}")
					return True
				else:
					print("Failed to fetch public keys")
					Logger.error(f"[CC LOG] Failed to fetch public keys: {e}", exc_info=True)	
					return False
			except Exception as e:
				print(f"Error fetching public keys: {e}")
				Logger.error(f"[CC LOG] Error fetching public keys: {e}", exc_info=True)	
				return False

		def validate_id_token(self, id_token):
			"""Validate the Firebase ID token locally."""
			if not self.public_keys:
				if not self.fetch_public_keys():
					return False

			#try:
			if "AA" == "AA":
				# Decode the header to get the `kid`
				Logger.info(f"[CC LOG] id_token: {id_token}")
				header, payload, signature = id_token.split('.')
				header_json = json.loads(base64.urlsafe_b64decode(header + '=='))
				Logger.info(f"[CC LOG] header_json: {header_json}")
				kid = header_json.get("kid")
				Logger.info(f"[CC LOG] kid: {kid}")

				if not kid or kid not in self.public_keys:
					print("Invalid 'kid' in token header or public key not found.")
					return False

				# Load the public key from the PEM certificate
				pem_certificate = self.public_keys[kid]
				Logger.info(f"[CC LOG] pem_certificate: {pem_certificate}")
				public_key = self._extract_public_key_from_pem(pem_certificate)
				Logger.info(f"[CC LOG] public_key: {public_key}")

				# Decode and verify the token
				payload_json = self._verify_token(header, payload, signature, public_key)
				Logger.info(f"[CC LOG] payload_json: {payload_json}")
				if payload_json and payload_json.get("aud") == self.firebase_project_id:
					Logger.info(f"[CC LOG] Valid token found!")
					return True  # Valid token found
				
				Logger.info(f"[CC LOG] NO valid token found!")
				return False

			'''
			except Exception as e:
				print(f"Error validating token: {e}")
				Logger.error(f"[CC LOG] Error validating token: {e}", exc_info=True)	
				return False
				'''

		def _extract_public_key_from_pem(self, pem_certificate):
			"""Extract the public key from a PEM certificate."""
			
			if "BB" == "BB":
			#try:
				certificate = load_pem_x509_certificate(pem_certificate.encode('utf-8'), default_backend())
				Logger.info(f"[CC LOG] certificate: {certificate}")
			'''
			except Exception as e:
				raise ValueError(f"certificate error: {e}")
				Logger.error(f"[CC LOG] certificate error: {e}", exc_info=True) # HEEERE
				'''
			
			#try:
			if "CC" == "CC":
				# Load the PEM certificate
				# certificate = load_pem_x509_certificate(pem_certificate.encode('utf-8'))

				# Extract the public key
				public_key = certificate.public_key()
				Logger.info(f"[CC LOG] public_key: {public_key}")
				return public_key
			'''
			except Exception as e:
				raise ValueError(f"Error extracting public key from PEM certificate: {e}")
				Logger.error(f"[CC LOG] Error extracting public key from PEM certificate: {e}", exc_info=True)
				'''

		def _verify_token(self, header, payload, signature, public_key):
			"""Verify the JWT token using the public key."""
			try:
				message = f"{header}.{payload}".encode('utf-8')
				signature_bytes = base64.urlsafe_b64decode(signature + '==')
				public_key.verify(
					signature_bytes,
					message,
					padding.PKCS1v15(),
					hashes.SHA256()
				)
				payload_json = json.loads(base64.urlsafe_b64decode(payload + '=='))
				# Verify expiration
				exp = datetime.fromtimestamp(payload_json.get('exp'))
				if exp < datetime.now():
					print("Token has expired.")
					Logger.info(f"[CC LOG] Token has expired")
					return None
				Logger.info(f"[CC LOG] Token verified using the public key")
				return payload_json
			except Exception as e:
				print(f"Invalid token: {e}")
				Logger.error(f"[CC LOG] Invalid token: {e}", exc_info=True)	
				return None
	
	
	
	class RateLimiter:
		def __init__(self, limit, period):
			self.limit = limit  # Maximum number of calls allowed
			self.period = period  # Time period in seconds
			self.calls = {}  # Dictionary to track calls per user

		def is_allowed(self, user_identifier):
			current_time = get_current_time()

			# Initialize the call list for the user if it doesn't exist
			if user_identifier not in self.calls:
				self.calls[user_identifier] = []

			# Remove outdated calls (outside the time window)
			self.calls[user_identifier] = [
				t for t in self.calls[user_identifier] if current_time - t <= self.period
			]

			# Check if the user is within the rate limit
			if len(self.calls[user_identifier]) < self.limit:
				self.calls[user_identifier].append(current_time)  # Log the current call
				return True
			return False

		def attempts_made(self, user_identifier):
			"""Returns the number of attempts made by the user within the time window."""
			current_time = get_current_time()
			if user_identifier in self.calls:
				# Filter out outdated attempts
				return len([
					t for t in self.calls[user_identifier] if current_time - t <= self.period
				])
			return 0
	
		def reset(self, user_identifier):
			"""Resets the attempts for a specific user."""
			if user_identifier in self.calls:
				self.calls[user_identifier] = []
				print("Rate limiter reset")
	
	
		
	Logger.info("[CC LOG] All classes loaded successfully!")

except Exception as e:
	Logger.error(f"[CC LOG] Failed to load classes: {e}", exc_info=True)
	



''' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Start of APP CONTENTS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - '''




try:
	class ConvoKeeper(App):
		def __init__(self, **kwargs):
			super().__init__(**kwargs)
			Logger.info("[CC LOG] Initiating the app...")
			
			self.init_database()
			self.firebase = pyrebase.initialize_app(firebase_config)
			self.firebase_db = self.firebase.database()
			self.session_manager = SessionManager()
			self.token_validator = TokenValidator(firebase_project_id=FIREBASE_PROJECT_ID)
			self.rate_limiter = RateLimiter(limit=5, period=60)
			
		def init_database(self):
			Logger.info("[CC LOG] Initializing the database...")
		
			self.conn = sqlite3.connect("convoKeeper.db")
			self.cursor = self.conn.cursor()
		
			try:
				self.cursor.execute("""
					CREATE TABLE IF NOT EXISTS users (
						firebase_uid TEXT PRIMARY KEY, 
						email TEXT NOT NULL UNIQUE,
						sync_status INTEGER DEFAULT 0,
						created_at TEXT DEFAULT CURRENT_TIMESTAMP,
						agreed_to_TnCs_and_PP TEXT
					)
				""")
				Logger.info("[CC LOG] Users table created!")
			except:
				Logger.error(f"[CC LOG] Failed to create users table: {e}", exc_info=True)
		
			try:
				self.cursor.execute("""
					CREATE TABLE IF NOT EXISTS favorites (
						firebase_uid TEXT NOT NULL PRIMARY KEY,
						category TEXT NOT NULL,
						FOREIGN KEY (firebase_uid) REFERENCES users(firebase_uid) ON DELETE CASCADE
					)
				""")
				Logger.info("[CC LOG] Favorites table created!")
			except:
				Logger.error(f"[CC LOG] Failed to create favorites table: {e}", exc_info=True)
		
			try:
				self.cursor.execute("""
					CREATE TABLE IF NOT EXISTS settings (
						firebase_uid TEXT NOT NULL PRIMARY KEY,
						narration_enabled TEXT NOT NULL,
						silence_detection_enabled TEXT NOT NULL,
						voice_recognition_language TEXT NOT NULL,
						awkward_silence_limit INTEGER NOT NULL,
						background_noise_calibration INTEGER NOT NULL,
						FOREIGN KEY (firebase_uid) REFERENCES users(firebase_uid) ON DELETE CASCADE
					)
				""")
				Logger.info("[CC LOG] Settings table created!")
				self.conn.commit()
			
			except:
				Logger.error(f"[CC LOG] Failed to create settings table: {e}", exc_info=True)
		
		
		try:
			def on_stop(self):
				Logger.info("[CC LOG] Closing the database connection because the app was stopped")
				self.conn.close()
		except:
			Logger.error(f"[CC LOG] Failed to close database properly: {e}", exc_info=True)
		
		try:
			def build(self):
				Logger.info("[CC LOG] Starting to build the app...")
				return self.create_main_layout()
			
			def create_main_layout(self):
				main_layout = CustomFloatLayout(size_hint=(1, 1), shape_type="rectangle", line_color=(0.30, 0.32, 0.36, 1), background_color=(0.11, 0.11, 0.13, 1))
				
				# Initiate variables
				self.agreed_to_TnCs_and_privacy_policy = "No"
				self.localId = None
				#self.localId = "kjf1Uz9Pt0T518THqCSQ3VZbqaw2"
				self.jiraAccountId = None
				self.introtext = "Pick a category, hit START and say goodbye to awkward silences!"
				self.all_categories = []
				self.favorite_categories = []
				self.favorite_categories_count = 0
				self.generated_categories = []
				self.selected_category = ""
				self.topics_in_selected_category = []
				self.current_topic = ""
				self.cat1 = ""
				self.cat2 = ""
				self.cat3 = ""
				self.cat4 = ""
				self.narration_enabled = True
				self.silence_detection_enabled = False
				self.awkward_silence_limit = 5
				self.voice_recognition_language = "en-US"
				self.background_noise_calibration = 0
				
				
				
				
				# PARENT WIDGET: Modal overlay
				self.widget_modal_overlay = ModalOverlay(app_ref=self, size_hint=(1, 1), pos_hint={'center_y': 0.5}) #  Main menu modal overlay
				self.widget_modal_overlay.bind(on_touch_down=self.slide_main_menu_and_toggle_modal_overlay)
				
				
				
				
				# PARENT WIDGET: Main menu
				self.widget_parent_menu_main_CFL = CustomFloatLayout(size_hint=(0.75, 1), pos_hint={'x': -1, 'center_y': 0.50}, shape_type="line_right", line_color=(0.30, 0.32, 0.36, 1), background_color=(0.11, 0.11, 0.13, 1))
		
				# 85, 127, 115, 96, 118 + 15
				self.widget_button_mainMenuItem_home_CB =         CustomButton(app_ref=self, text="Home",      size_hint=(0.45, 0.032), pos_hint={'x': 0.05, 'center_y': 0.94}, button_type="Menu", background_color_flicker=(0, 0, 0, 0), font_size=36, shape_type="line_menu", line_width=1.5, halign="left", valign="bottom")
				self.widget_button_mainMenuItem_favorites_CB =    CustomButton(app_ref=self, text="Favorites", size_hint=(0.45, 0.032), pos_hint={'x': 0.05, 'center_y': 0.90}, button_type="Menu", background_color_flicker=(0, 0, 0, 0), font_size=36, shape_type="line_menu", line_width=1.5, halign="left", valign="bottom")
				self.widget_button_mainMenuItem_lab_CB =          CustomButton(app_ref=self, text="Laboratory",size_hint=(0.45, 0.032), pos_hint={'x': 0.05, 'center_y': 0.86}, button_type="Menu", background_color_flicker=(0, 0, 0, 0), font_size=36, shape_type="line_menu", line_width=1.5, halign="left", valign="bottom")
				self.widget_button_mainMenuItem_settings_CB =     CustomButton(app_ref=self, text="Settings",  size_hint=(0.45, 0.032), pos_hint={'x': 0.05, 'center_y': 0.82}, button_type="Menu", background_color_flicker=(0, 0, 0, 0), font_size=36, shape_type="line_menu", line_width=1.5, halign="left", valign="bottom")
				self.widget_button_mainMenuItem_support_CB =      CustomButton(app_ref=self, text="Support",   size_hint=(0.45, 0.032), pos_hint={'x': 0.05, 'center_y': 0.78}, button_type="Menu", background_color_flicker=(0, 0, 0, 0), font_size=36, shape_type="line_menu", line_width=1.5, halign="left", valign="bottom")
				self.widget_button_mainMenuItem_signInAndOut_CB = CustomButton(app_ref=self, text="Sign in",   size_hint=(0.45, 0.032), pos_hint={'x': 0.05, 'center_y': 0.74}, button_type="Menu", background_color_flicker=(0, 0, 0, 0), font_size=36, shape_type="line_menu", line_width=1.5, halign="left", valign="bottom")
				
				self.widget_button_mainMenuItem_home_CB.bind(on_release=self.hide_modal_overlay_AND_hide_main_menu_AND_slide_widgets_left_AND_toggle_pages)
				self.widget_button_mainMenuItem_favorites_CB.bind(on_release=self.render_favorites_list)
				self.widget_button_mainMenuItem_favorites_CB.bind(on_release=self.hide_modal_overlay_AND_hide_main_menu_AND_slide_widgets_left_AND_toggle_pages)
				self.widget_button_mainMenuItem_lab_CB.bind(on_release=self.hide_modal_overlay_AND_hide_main_menu_AND_slide_widgets_left_AND_toggle_pages)
				self.widget_button_mainMenuItem_settings_CB.bind(on_release=self.hide_modal_overlay_AND_hide_main_menu_AND_slide_widgets_left_AND_toggle_pages)
				self.widget_button_mainMenuItem_support_CB.bind(on_release=self.hide_modal_overlay_AND_hide_main_menu_AND_slide_widgets_left_AND_toggle_pages)
				self.widget_button_mainMenuItem_signInAndOut_CB.bind(on_release=self.hide_modal_overlay_AND_hide_main_menu_AND_slide_widgets_left_AND_toggle_pages)
				'''
				self.widget_button_mainMenuItem_signInAndOut_CB.bind(on_release=self.sign_in_out_button_pushed)
				'''
				
				self.widget_parent_menu_main_CFL.add_widget(self.widget_button_mainMenuItem_home_CB)
				self.widget_parent_menu_main_CFL.add_widget(self.widget_button_mainMenuItem_favorites_CB)
				self.widget_parent_menu_main_CFL.add_widget(self.widget_button_mainMenuItem_lab_CB)
				self.widget_parent_menu_main_CFL.add_widget(self.widget_button_mainMenuItem_settings_CB)
				self.widget_parent_menu_main_CFL.add_widget(self.widget_button_mainMenuItem_signInAndOut_CB)
				self.widget_parent_menu_main_CFL.add_widget(self.widget_button_mainMenuItem_support_CB)
				
				
					
				
				# PARENT WIDGET: Menu bar, top
				self.widget_parent_menu_top_CBL = CustomBoxLayout(app_ref=self, orientation='horizontal', padding=[25, 0, 25, 0], spacing=0, size_hint=(1, 0.1), pos_hint={'center_x': 0.5, 'top': 1}, background_color=(0.11, 0.11, 0.13, 1), line_color=(0.30, 0.32, 0.36, 1), shape_type="line_bottom", line_width=1)
		
				self.widget_button_hamburger_CB = CustomButton(app_ref=self, text='\uf0c9', size_hint=(0.12, 0.5), pos_hint={'left': 1, 'center_y': 0.5}, font_size=58, background_color_flicker=(0, 0, 0, 0), font_name=GLOBAL_FONT_UNICODE, line_color=(0, 0, 0, 0), halign="left")
				self.widget_image_logo_IMG = Image(source='images/logo.png', size_hint=(0.76, 0.7), pos_hint={'center_x': 0.5, 'center_y': 0.5})
				self.widget_button_signInAndProfile_CB = CustomButton(app_ref=self, text='Sign in', size_hint=(0.12, 0.5), pos_hint={'right': 1, 'center_y': 0.5}, font_size=28, background_color_flicker=(0, 0, 0, 0), font_name=GLOBAL_FONT_BOLD, line_color=(0, 0, 0, 0), halign="right")
		
				self.widget_button_hamburger_CB.bind(on_release=self.show_modal_overlay_AND_show_main_menu_AND_slide_widgets_right_AND_toggle_pages)
				self.widget_button_signInAndProfile_CB.bind(on_release=self.update_layout_of_main_menu_signIn_button)
				self.widget_button_signInAndProfile_CB.bind(on_release=self.sign_in_profile_button_pushed)
		
				self.widget_parent_menu_top_CBL.add_widget(self.widget_button_hamburger_CB)
				self.widget_parent_menu_top_CBL.add_widget(self.widget_image_logo_IMG)
				self.widget_parent_menu_top_CBL.add_widget(self.widget_button_signInAndProfile_CB)
				
				
				
				
				# PARENT WIDGET: App body
				self.widget_parent_body_CBL = CustomBoxLayout(app_ref=self, orientation='vertical', padding=25, spacing=0, size_hint=(1, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.5}, shape_type="rectangle")
		
				# Child widget layouts 
				self.widget_label_topic_CL = CustomLabel(app_ref=self, text=f"{self.introtext}", size_hint=(1, 0.35), font_size=45, shape_type="rectangle")
				self.widget_button_refresh_CFL = CustomFloatLayout(size_hint=(1, 0.1), shape_type="rectangle")
				self.widget_category_buttons_CGL = CustomGridLayout(cols=2, spacing=15, size_hint=(1, 0.35), shape_type="rectangle")
				self.widget_button_start_CFL = CustomFloatLayout(size_hint=(1, 0.20), shape_type="rectangle")
		
				# Child widgets
				self.widget_button_refresh_CB = CustomButton(app_ref=self, text='\uf021', size_hint=(0.15, 0.8), pos_hint={'right': 1, 'center_y': 0.5}, font_size=50, button_type='Refresh', background_color_flicker=(0, 0, 0, 0), font_name=GLOBAL_FONT_UNICODE)
				self.widget_category_button_cat1_CB = CustomButton(app_ref=self, text=self.cat1, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.1}, button_type='Category', color=(0.15, 0.16, 0.18, 1), background_color=(0.83, 0.84, 0.85, 1), background_color_selected=(0.2, 0.64, 0.81, 1), font_name=GLOBAL_FONT_BOLD, corner_radius=50)
				self.widget_category_button_cat2_CB = CustomButton(app_ref=self, text=self.cat2, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.1}, button_type='Category', color=(0.15, 0.16, 0.18, 1), background_color=(0.83, 0.84, 0.85, 1), background_color_selected=(0.2, 0.64, 0.81, 1), font_name=GLOBAL_FONT_BOLD, corner_radius=50)
				self.widget_category_button_cat3_CB = CustomButton(app_ref=self, text=self.cat3, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.1}, button_type='Category', color=(0.15, 0.16, 0.18, 1), background_color=(0.83, 0.84, 0.85, 1), background_color_selected=(0.2, 0.64, 0.81, 1), font_name=GLOBAL_FONT_BOLD, corner_radius=50)
				self.widget_category_button_cat4_CB = CustomButton(app_ref=self, text=self.cat4, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.1}, button_type='Category', color=(0.15, 0.16, 0.18, 1), background_color=(0.83, 0.84, 0.85, 1), background_color_selected=(0.2, 0.64, 0.81, 1), font_name=GLOBAL_FONT_BOLD, corner_radius=50)
				self.widget_button_start_CB = CustomButton(app_ref=self, text='START', size_hint=(0.32, 0.42), pos_hint={'center_x': 0.5, 'center_y': 0.35}, font_size=50, background_color=(0.10, 0.70, 0.46, 1), corner_radius=35)
		
				#Bind buttons
				self.widget_button_refresh_CB.bind(on_release=self.generate_categories)
				'''
				self.widget_button_refresh_CB.bind(on_release=self.stop_speech_recognition)
				'''
				self.widget_category_button_cat1_CB.bind(on_release=self.generate_topic)
				self.widget_category_button_cat2_CB.bind(on_release=self.generate_topic)
				self.widget_category_button_cat3_CB.bind(on_release=self.generate_topic)
				self.widget_category_button_cat4_CB.bind(on_release=self.generate_topic)
				self.widget_button_start_CB.bind(on_release=self.start_game)
		
		
		
				# Add buttons to child widget layouts
				self.widget_button_refresh_CFL.add_widget(self.widget_button_refresh_CB)
				self.widget_category_buttons_CGL.add_widget(self.widget_category_button_cat1_CB)
				self.widget_category_buttons_CGL.add_widget(self.widget_category_button_cat2_CB)
				self.widget_category_buttons_CGL.add_widget(self.widget_category_button_cat3_CB)
				self.widget_category_buttons_CGL.add_widget(self.widget_category_button_cat4_CB)
				self.widget_button_start_CFL.add_widget(self.widget_button_start_CB)
		
				# Add child widgets to parent widget
				self.widget_parent_body_CBL.add_widget(self.widget_label_topic_CL) 
				self.widget_parent_body_CBL.add_widget(self.widget_button_refresh_CFL)
				self.widget_parent_body_CBL.add_widget(self.widget_category_buttons_CGL)
				self.widget_parent_body_CBL.add_widget(self.widget_button_start_CFL)
				
				
				
				
				# PARENT WIDGET: Menu bar, bottom
				self.widget_parent_menu_bottom_CBL = CustomBoxLayout(app_ref=self, orientation='vertical', padding=[0, 20, 0, 20], spacing=0, size_hint=(1, 0.1), pos_hint={'center_x': 0.5, 'y': 0}, shape_type="rectangle")
		
				self.widget_menu_bottom_CFL = CustomFloatLayout(size_hint=(0.7, 1), pos_hint={'center_x': 0.5, 'y': 0}, background_color=(0.11, 0.11, 0.13, 1), shape_type="rectangle_rounded")

				self.widget_button_home_CB = CustomButton(app_ref=self, text='\uf015', font_name=GLOBAL_FONT_UNICODE, size_hint=(0.15, 0.65), pos_hint={'x': 0.0750000, 'center_y': 0.5}, font_size=35, background_color=(0.5, 0.5, 1, 1))	# \uf015
				self.widget_button_favo_CB = CustomButton(app_ref=self, text='\uf005', font_name=GLOBAL_FONT_UNICODE, size_hint=(0.15, 0.65), pos_hint={'x': 0.3100000, 'center_y': 0.5}, font_size=35, background_color=(0.5, 0.5, 1, 1))	# \uf005
				self.widget_button_lab_CB =  CustomButton(app_ref=self, text= '\uf0c3', font_name=GLOBAL_FONT_UNICODE, size_hint=(0.15, 0.65), pos_hint={'right': 0.690, 'center_y': 0.5}, font_size=35, background_color=(0.5, 0.5, 1, 1))	# \uf007
				self.widget_button_sett_CB = CustomButton(app_ref=self, text='\u2699', font_name=GLOBAL_FONT_UNICODE, size_hint=(0.15, 0.65), pos_hint={'right': 0.925, 'center_y': 0.5}, font_size=35, background_color=(0.5, 0.5, 1, 1))	# \u2699
				
				self.widget_button_home_CB.bind(on_release=self.hide_modal_overlay_AND_hide_main_menu_AND_slide_widgets_left_AND_toggle_pages)
				self.widget_button_home_CB.bind(on_release=self.update_layout_of_main_menu_home_button)
				
				self.widget_button_favo_CB.bind(on_release=self.show_favorites_page)
				self.widget_button_favo_CB.bind(on_release=self.update_layout_of_main_menu_favorite_button)
				self.widget_button_favo_CB.bind(on_release=self.render_favorites_list)
				self.widget_button_lab_CB.bind(on_release=self.show_lab_page)
				self.widget_button_favo_CB.bind(on_release=self.update_layout_of_main_menu_lab_button)
				self.widget_button_sett_CB.bind(on_release=self.show_settings_page)
				self.widget_button_sett_CB.bind(on_release=self.update_layout_of_main_menu_settings_button)
		
				self.widget_menu_bottom_CFL.add_widget(self.widget_button_home_CB)
				self.widget_menu_bottom_CFL.add_widget(self.widget_button_favo_CB)
				self.widget_menu_bottom_CFL.add_widget(self.widget_button_lab_CB)
				self.widget_menu_bottom_CFL.add_widget(self.widget_button_sett_CB)
		
				self.widget_parent_menu_bottom_CBL.add_widget(self.widget_menu_bottom_CFL)
				
				
				
				
				# PARENT WIDGET: Register page
				self.widget_parent_page_register_CFL = CustomFloatLayout(size_hint=(1, 0.8), pos_hint={'x': 1, 'center_y': 0.50}, shape_type="rectangle", background_color=(0.15, 0.16, 0.18, 1))
		
				self.widget_button_close_register_CB = CustomButton(app_ref=self,       text='\uf00d',               size_hint=(0.05, 0.05), pos_hint={'center_x': 0.9, 'center_y': 0.95}, font_size=30, font_name=GLOBAL_FONT_UNICODE, background_color_flicker=(0, 0, 0, 0), shape_type="rectangle")
				self.widget_label_register_CL =        CustomLabel(app_ref=self,        text="Register",             size_hint=(1.00, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.90}, font_size=50, font_name=GLOBAL_FONT_BOLD, halign="center")
				self.widget_textInput_regEmail =       CustomTextInput(app_ref=self,    hint_text='E-mail address',  size_hint=(0.90, 0.05), pos_hint={'center_x': 0.5, 'center_y': 0.80}, multiline=False)
				self.widget_textInput_regPassword =    CustomTextInput(app_ref=self,    hint_text='Password',        size_hint=(0.90, 0.05), pos_hint={'center_x': 0.5, 'center_y': 0.73}, multiline=False, password=True)
				self.widget_textInput_regPwRepeat =    CustomTextInput(app_ref=self,    hint_text='Repeat password', size_hint=(0.90, 0.05), pos_hint={'center_x': 0.5, 'center_y': 0.66}, multiline=False, password=True)
				self.widget_label_agree_CL =           CustomLabel(app_ref=self,        text=f"I agree to [ref=T&Cs][u]Terms and Conditions[/u][/ref] and [ref=PP][u] Privacy Policy[/u][/ref]", size_hint=(0.80, 0.050), pos_hint={'x': 0.05, 'center_y': 0.59}, halign="left", font_size=26)
				self.toggle_button_agree_CTB =         CustomToggleButton(app_ref=self, toggle_name="Agreed to T&C and PP",                             size_hint=(0.11, 0.035), pos_hint={'center_x': 0.88, 'center_y': 0.59})
				self.widget_button_register_CB =       CustomButton(app_ref=self,       text='Sign up',              size_hint=(0.90, 0.06), pos_hint={'center_x': 0.5, 'center_y': 0.50}, font_size=36, font_name=GLOBAL_FONT_BOLD, background_color=(0.2, 0.64, 0.81, 1), shape_type="rectangle_rounded")
				self.widget_label_reg_warning_CL =     CustomLabel(app_ref=self,        text="",                     size_hint=(1.00, 0.05), pos_hint={'center_x': 0.5, 'center_y': 0.40}, font_name=GLOBAL_FONT_BOLD, color=(1, 0, 0, 1), font_size=28, halign="center")
		
				self.widget_button_close_register_CB.bind(on_release=self.hide_register_page)
				self.widget_button_close_register_CB.bind(on_release=self.hide_signIn_page)
				self.widget_button_close_register_CB.bind(on_release=self.update_layout_of_main_menu_home_button)
				self.widget_label_agree_CL.bind(on_ref_press=self.open_url)
				self.toggle_button_agree_CTB.bind(on_release=self.toggle_button_toggled)
				self.widget_button_register_CB.bind(on_release=self.register_user)
		
				self.widget_parent_page_register_CFL.add_widget(self.widget_button_close_register_CB)
				self.widget_parent_page_register_CFL.add_widget(self.widget_label_register_CL)
				self.widget_parent_page_register_CFL.add_widget(self.widget_textInput_regEmail)
				self.widget_parent_page_register_CFL.add_widget(self.widget_textInput_regPassword)
				self.widget_parent_page_register_CFL.add_widget(self.widget_textInput_regPwRepeat)
				self.widget_parent_page_register_CFL.add_widget(self.widget_label_agree_CL)
				self.widget_parent_page_register_CFL.add_widget(self.toggle_button_agree_CTB)
				self.widget_parent_page_register_CFL.add_widget(self.widget_button_register_CB)
				self.widget_parent_page_register_CFL.add_widget(self.widget_label_reg_warning_CL)
				
				
				
				
				# PARENT WIDGET: Sign in page
				self.widget_parent_page_signIn_CFL = CustomFloatLayout(size_hint=(1, 0.8), pos_hint={'x': 1, 'center_y': 0.50}, shape_type="rectangle", background_color=(0.15, 0.16, 0.18, 1))
		
				self.widget_button_close_signIn_CB =  CustomButton(app_ref=self,    text='\uf00d',                                     size_hint=(0.05, 0.050), pos_hint={'center_x': 0.9, 'center_y': 0.95}, font_size=30, font_name=GLOBAL_FONT_UNICODE, background_color_flicker=(0, 0, 0, 0), shape_type="rectangle")
				self.widget_label_signIn_CL =         CustomLabel(app_ref=self,     text="Sign in",                                    size_hint=(1.00, 0.100), pos_hint={'center_x': 0.5, 'center_y': 0.90}, font_size=50, font_name=GLOBAL_FONT_BOLD, halign="center")
				self.widget_textInput_entUsername =   CustomTextInput(app_ref=self, hint_text='E-mail address',                        size_hint=(0.90, 0.050), pos_hint={'center_x': 0.5, 'center_y': 0.80}, shape_type="rectangle_rounded", multiline=False)
				self.widget_textInput_entPassword =   CustomTextInput(app_ref=self, hint_text='Password',                              size_hint=(0.90, 0.050), pos_hint={'center_x': 0.5, 'center_y': 0.73}, shape_type="rectangle_rounded", multiline=False, password=True)
				self.widget_label_forgotPassword_CB = CustomButton(app_ref=self,    text="[u]Forgot password?[/u]",                    size_hint=(0.40, 0.025), pos_hint={'right': 0.9500, 'center_y': 0.69}, font_size=28, background_color_flicker=(0, 0, 0, 0), halign="right")
				self.widget_button_login_CB =         CustomButton(app_ref=self,    text='Sign in',                                    size_hint=(0.90, 0.060), pos_hint={'center_x': 0.5, 'center_y': 0.63}, font_size=36, font_name=GLOBAL_FONT_BOLD, background_color=(0.2, 0.64, 0.81, 1), shape_type="rectangle_rounded")
				self.widget_label_registerNow_CB =    CustomButton(app_ref=self,    text="Don't have an account? [u]Register now[/u]", size_hint=(0.90, 0.050), pos_hint={'center_x': 0.5, 'center_y': 0.53}, background_color_flicker=(0, 0, 0, 0), halign="left", shape_type="rectangle")
				self.widget_label_warning_signIn_CL = CustomLabel(app_ref=self,     text="",                                           size_hint=(1.00, 0.050), pos_hint={'center_x': 0.5, 'center_y': 0.43}, font_name=GLOBAL_FONT_BOLD, color=(1, 0, 0, 1), halign="center")
		
				self.widget_button_close_signIn_CB.bind(on_release=self.hide_signIn_page)
				self.widget_button_close_signIn_CB.bind(on_release=self.update_layout_of_main_menu_home_button)
				'''
				self.widget_label_forgotPassword_CB.bind(on_release=self.forgot_password)
				'''
				self.widget_button_login_CB.bind(on_release=self.sign_in)
				self.widget_label_registerNow_CB.bind(on_release=self.show_register_page)
				self.widget_label_registerNow_CB.bind(on_release=self.hide_signIn_page)
		
				self.widget_parent_page_signIn_CFL.add_widget(self.widget_button_close_signIn_CB)
				self.widget_parent_page_signIn_CFL.add_widget(self.widget_label_signIn_CL)
				self.widget_parent_page_signIn_CFL.add_widget(self.widget_textInput_entUsername)
				self.widget_parent_page_signIn_CFL.add_widget(self.widget_textInput_entPassword)
				self.widget_parent_page_signIn_CFL.add_widget(self.widget_label_forgotPassword_CB)
				self.widget_parent_page_signIn_CFL.add_widget(self.widget_button_login_CB)
				self.widget_parent_page_signIn_CFL.add_widget(self.widget_label_registerNow_CB)
				self.widget_parent_page_signIn_CFL.add_widget(self.widget_label_warning_signIn_CL)
				
				
				
				
				# PARENT WIDGET: Settings page
				self.widget_parent_page_settings_CFL = CustomFloatLayout(size_hint=(1, 0.8), pos_hint={'x': 1, 'center_y': 0.50}, shape_type="rectangle", background_color=(0.15, 0.16, 0.18, 1))
		
				self.widget_button_close_settings_CB =  CustomButton(app_ref=self,      text='\uf00d',                                        size_hint=(0.050, 0.050), pos_hint={'center_x': 0.90, 'center_y': 0.95}, font_name=GLOBAL_FONT_UNICODE, shape_type="rectangle", font_size=30, background_color_flicker=(0, 0, 0, 0))
				self.widget_label_settings_CL =         CustomLabel(app_ref=self,       text="Settings",                                      size_hint=(1.000, 0.100), pos_hint={'center_x': 0.5, 'center_y': 0.90}, halign="center", font_size=50, font_name=GLOBAL_FONT_BOLD)
				self.widget_button_close_settings_CB.bind(on_release=self.hide_settings_page)
				self.widget_button_close_settings_CB.bind(on_release=self.update_layout_of_main_menu_home_button)
		
				# Narration
				self.widget_label_tts_enabled_CL =      CustomLabel(app_ref=self,        text="Narration enabled:",                           size_hint=(0.600, 0.050), pos_hint={'x': 0.05, 'center_y': 0.80}, halign="left")
				self.toggle_button_tts_enabled_CB =     CustomToggleButton(app_ref=self, toggle_name="Narration enabled",                     size_hint=(0.110, 0.035), pos_hint={'center_x': 0.82, 'center_y': 0.80})
				self.toggle_button_tts_enabled_CB.bind(on_release=self.toggle_button_toggled)
		
				# Silence detection
				self.widget_label_sd_enabled_CL =       CustomLabel(app_ref=self,         text="Silence detection enabled:",                  size_hint=(0.600, 0.050), pos_hint={'x': 0.05, 'center_y': 0.73}, halign="left")
				self.toggle_button_sd_enabled_CB =      CustomToggleButton(app_ref=self,  toggle_name="Silence detection enabled",            size_hint=(0.110, 0.035), pos_hint={'center_x': 0.82, 'center_y': 0.73})
				self.toggle_button_sd_enabled_CB.bind(on_release=self.toggle_button_toggled)
		
				# Voice recognition language
				self.widget_label_vr_language_CL = CustomLabel(app_ref=self,              text="Silence detection language:",                 size_hint=(0.600, 0.050), pos_hint={'x': 0.05, 'center_y': 0.66}, halign="left")
				self.spinner_vr_language_SP = Spinner(values=('en-US', 'sv-SE'),      text=self.voice_recognition_language,               size_hint=(0.220, 0.045), pos_hint={'center_x': 0.82, 'center_y': 0.66})
				self.spinner_vr_language_SP.bind(text=self.spinner_button_spinned)
		
				# Awkward silence limit
				self.widget_label_max_silence_CL = CustomLabel(app_ref=self, text=f"Awkward silence limit ({self.awkward_silence_limit} s):", size_hint=(0.600, 0.050), pos_hint={'x': 0.05, 'center_y': 0.59}, halign="left")
				self.slider_max_silence_SL = Slider(value=self.awkward_silence_limit,                                                         size_hint=(0.980, 0.035), pos_hint={'center_x': 0.5, 'center_y': 0.54}, min=5, max=60)
				self.slider_max_silence_SL.bind(value=self.slider_button_slided)
		
				# Background noise calibration
				self.widget_label_bg_noise_cal_CL = CustomLabel(app_ref=self, text=f"Background noise calibration ({self.background_noise_calibration}):", size_hint=(0.9, 0.050), pos_hint={'x': 0.05, 'center_y': 0.47}, halign="left")
				self.slider_bg_noise_cal_SL = Slider(value=self.background_noise_calibration,                                                 size_hint=(0.980, 0.035), pos_hint={'center_x': 0.5, 'center_y': 0.42}, min=-150, max=150)
				self.slider_bg_noise_cal_SL.bind(value=self.slider_button_slided)
		
				# Button
				self.widget_button_save_settings_CB = CustomButton(app_ref=self, text='Save settings',                                        size_hint=(0.900, 0.06), pos_hint={'center_x': 0.5, 'center_y': 0.32}, font_name=GLOBAL_FONT_BOLD, font_size=36, shape_type="rectangle_rounded", background_color=(0.2, 0.64, 0.81, 1)) # color=(0.11, 0.11, 0.13, 1)
				self.widget_label_save_set_warning_CL = CustomLabel(app_ref=self, text="",                                                    size_hint=(1.000, 0.05), pos_hint={'center_x': 0.5, 'center_y': 0.22}, halign="center", font_name=GLOBAL_FONT_BOLD, color=(0.10, 0.70, 0.46, 1))
				self.widget_button_save_settings_CB.bind(on_release=self.save_settings)
		
				self.widget_parent_page_settings_CFL.add_widget(self.widget_button_close_settings_CB)
				self.widget_parent_page_settings_CFL.add_widget(self.widget_label_settings_CL)
				self.widget_parent_page_settings_CFL.add_widget(self.widget_label_tts_enabled_CL)
				self.widget_parent_page_settings_CFL.add_widget(self.toggle_button_tts_enabled_CB)
				self.widget_parent_page_settings_CFL.add_widget(self.widget_label_sd_enabled_CL)
				self.widget_parent_page_settings_CFL.add_widget(self.toggle_button_sd_enabled_CB)
				self.widget_parent_page_settings_CFL.add_widget(self.widget_label_max_silence_CL)
				self.widget_parent_page_settings_CFL.add_widget(self.slider_max_silence_SL)
				self.widget_parent_page_settings_CFL.add_widget(self.widget_label_vr_language_CL)
				self.widget_parent_page_settings_CFL.add_widget(self.spinner_vr_language_SP)
				self.widget_parent_page_settings_CFL.add_widget(self.widget_label_bg_noise_cal_CL)
				self.widget_parent_page_settings_CFL.add_widget(self.slider_bg_noise_cal_SL)
				self.widget_parent_page_settings_CFL.add_widget(self.widget_button_save_settings_CB)
				self.widget_parent_page_settings_CFL.add_widget(self.widget_label_save_set_warning_CL)
				
				
				
				
				# PARENT WIDGET: Favorites page
				self.widget_parent_page_favorites_CFL = CustomFloatLayout(size_hint=(1, 0.8), pos_hint={'x': 1, 'center_y': 0.50}, shape_type="rectangle", background_color=(0.15, 0.16, 0.18, 1))
		
				self.widget_button_close_favorites_CB = CustomButton(app_ref=self,    text='\uf00d',          size_hint=(0.05, 0.05), pos_hint={'center_x': 0.90, 'center_y': 0.95}, shape_type="rectangle", font_size=30, font_name=GLOBAL_FONT_UNICODE, background_color_flicker=(0, 0, 0, 0))
				self.widget_label_favorites_CL =        CustomLabel(app_ref=self,     text="Favorites",       size_hint=(1.00, 0.10), pos_hint={'center_x': 0.50, 'center_y': 0.90}, halign="center", font_size=50, font_name=GLOBAL_FONT_BOLD)
				self.widget_favorites_page_CBL =        CustomBoxLayout(app_ref=self, orientation='vertical', size_hint=(1.00, None), pos_hint={'center_x': 0.50, 'top': 0.85}, padding=0, spacing=14, shape_type="rectangle")
				
				self.widget_button_close_favorites_CB.bind(on_release=self.hide_favorites_page)
				#self.widget_button_close_favorites_CB.bind(on_release=self.update_layout_of_main_menu_home_button)
		
				self.widget_parent_page_favorites_CFL.add_widget(self.widget_button_close_favorites_CB)
				self.widget_parent_page_favorites_CFL.add_widget(self.widget_label_favorites_CL)
				self.widget_parent_page_favorites_CFL.add_widget(self.widget_favorites_page_CBL)
				
				
				
				
				# PARENT WIDGET: Laboratory page
				self.widget_parent_page_lab_CFL = CustomFloatLayout(size_hint=(1, 0.8), pos_hint={'x': 1, 'center_y': 0.50}, shape_type="rectangle", background_color=(0.15, 0.16, 0.18, 1))
		
				self.widget_button_close_lab_CB =    CustomButton(app_ref=self,    text='\uf00d',                                       size_hint=(0.05, 0.05), pos_hint={'center_x': 0.90, 'center_y': 0.95}, shape_type="rectangle", font_size=30, font_name=GLOBAL_FONT_UNICODE, background_color_flicker=(0, 0, 0, 0))
				self.widget_label_lab_CL =           CustomLabel(app_ref=self,     text="Laboratory",                                   size_hint=(1.00, 0.10), pos_hint={'center_x': 0.50, 'center_y': 0.90}, halign="center", font_size=50, font_name=GLOBAL_FONT_BOLD)
				self.widget_label_info_lab_CL =      CustomLabel(app_ref=self,     text="Create your own categories and topics!",       size_hint=(1.00, 0.05), pos_hint={'center_x': 0.50, 'center_y': 0.80}, halign="center", font_name=GLOBAL_FONT_BOLD)
				self.widget_textInput_category_CTI = CustomTextInput(app_ref=self, hint_text='Chose category name',                     size_hint=(0.90, 0.05), pos_hint={'center_x': 0.50, 'center_y': 0.73}, shape_type="rectangle_rounded", multiline=False, halign="center", padding=[10, 0, 0, 0])
				self.widget_textInput_topic_CTI =    CustomTextInput(app_ref=self, hint_text='Then enter a topic (max. 75 characters)', size_hint=(0.90, 0.05), pos_hint={'center_x': 0.50, 'center_y': 0.66}, shape_type="rectangle_rounded", multiline=False, halign="center", padding=[10, 0, 0, 0])
				self.widget_button_create_CB =       CustomButton(app_ref=self,    text='Create!',                                      size_hint=(0.90, 0.06), pos_hint={'center_x': 0.50, 'center_y': 0.58}, font_size=36, font_name=GLOBAL_FONT_BOLD, background_color=(0.2, 0.64, 0.81, 1), shape_type="rectangle_rounded")
				self.widget_label_warning_lab_CL =   CustomLabel(app_ref=self,     text="",                                             size_hint=(1.00, 0.05), pos_hint={'center_x': 0.50, 'center_y': 0.52}, font_name=GLOBAL_FONT_BOLD, color=(1, 0, 0, 1), halign="center")
				self.widget_labResults_SV =          ScrollView(size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.50})
				self.widget_labResults_CFL =         CustomFloatLayout(size_hint=(0.9, 0.45), pos_hint={'center_x': 0.5, 'center_y': 0.26}, shape_type="rectangle", background_color=(0, 0, 0, 0))
				self.widget_label_note_lab_CL =      CustomLabel(app_ref=self,     text="",                                             size_hint=(1.00, 0.05), pos_hint={'center_x': 0.50, 'center_y': 0.01}, halign="center", font_size = 28)
		
				self.widget_button_close_lab_CB.bind(on_release=self.hide_lab_page)
				self.widget_button_close_lab_CB.bind(on_release=self.update_layout_of_main_menu_home_button)
				self.widget_button_create_CB.bind(on_release=self.create_topic)
		
		
				self.widget_parent_page_lab_CFL.add_widget(self.widget_button_close_lab_CB)
				self.widget_parent_page_lab_CFL.add_widget(self.widget_label_lab_CL)
				self.widget_parent_page_lab_CFL.add_widget(self.widget_label_info_lab_CL)
				self.widget_parent_page_lab_CFL.add_widget(self.widget_textInput_category_CTI)
				self.widget_parent_page_lab_CFL.add_widget(self.widget_textInput_topic_CTI)
				self.widget_parent_page_lab_CFL.add_widget(self.widget_button_create_CB)
				self.widget_parent_page_lab_CFL.add_widget(self.widget_label_warning_lab_CL)
				self.widget_parent_page_lab_CFL.add_widget(self.widget_labResults_CFL)
				self.widget_parent_page_lab_CFL.add_widget(self.widget_label_note_lab_CL)
				
				
				
				
				# PARENT WIDGET: Session expired
				self.widget_session_expired_CFL = CustomFloatLayout(size_hint=(0.8, 0.5), pos_hint={'x': 1, 'center_y': 0.50}, shape_type="rectangle_rounded", background_color=(0.15, 0.16, 0.18, 1), line_color=(1, 1, 1, 1))
		
				self.widget_button_close_session_expired_CB = CustomButton(app_ref=self,    text='\uf00d',                   size_hint=(0.05, 0.050), pos_hint={'center_x': 0.90, 'center_y': 0.90}, font_size=30, font_name=GLOBAL_FONT_UNICODE, background_color_flicker=(0, 0, 0, 0), shape_type="rectangle")
				self.widget_label_session_expired_header_CL = CustomLabel(app_ref=self,     text="Session expired",          size_hint=(1.00, 0.100), pos_hint={'center_x': 0.50, 'center_y': 0.70}, font_size=50, font_name=GLOBAL_FONT_BOLD, halign="center")
				self.widget_label_session_expired_body_CL =   CustomLabel(app_ref=self,     text="You have been signed out", size_hint=(1.00, 0.050), pos_hint={'center_x': 0.50, 'center_y': 0.50}, font_name=GLOBAL_FONT_BOLD, halign="center")
				self.widget_button_to_signIn_page_CB =        CustomButton(app_ref=self,    text='To sign in page',          size_hint=(0.90, 0.100), pos_hint={'center_x': 0.50, 'center_y': 0.20}, font_size=36, font_name=GLOBAL_FONT_BOLD, background_color=(0.2, 0.64, 0.81, 1), shape_type="rectangle_rounded")
		
				self.widget_button_close_session_expired_CB.bind(on_release=self.close_session_expired_popup)
				self.widget_button_to_signIn_page_CB.bind(on_release=self.close_session_expired_popup)
		
				self.widget_session_expired_CFL.add_widget(self.widget_button_close_session_expired_CB)
				self.widget_session_expired_CFL.add_widget(self.widget_label_session_expired_header_CL)
				self.widget_session_expired_CFL.add_widget(self.widget_label_session_expired_body_CL)
				self.widget_session_expired_CFL.add_widget(self.widget_button_to_signIn_page_CB)
				
				
				
				
				# PARENT WIDGET: Notification banner
				self.widget_notification_banner_CFL = CustomFloatLayout(size_hint=(1, 0.03), pos_hint={'x': 1, 'center_y': 0.89}, shape_type="rectangle", background_color=(0.97, 0.53, 0.20, 1))
				self.widget_notification_banner_CL =  CustomLabel(app_ref=self, text="", size_hint=(1, 1), pos_hint={'center_x': 0.50, 'center_y': 0.50}, font_name=GLOBAL_FONT_BOLD, halign="center", font_size=30)
				self.widget_notification_banner_CFL.add_widget(self.widget_notification_banner_CL)
				
				
				
				
				# Add parent widgets to main layout
				main_layout.add_widget(self.widget_parent_menu_top_CBL)
				main_layout.add_widget(self.widget_parent_body_CBL)
				main_layout.add_widget(self.widget_parent_menu_bottom_CBL)
				main_layout.add_widget(self.widget_parent_page_register_CFL)
				main_layout.add_widget(self.widget_parent_page_signIn_CFL)
				main_layout.add_widget(self.widget_parent_page_settings_CFL)
				main_layout.add_widget(self.widget_parent_page_favorites_CFL)
				main_layout.add_widget(self.widget_parent_page_lab_CFL)
				main_layout.add_widget(self.widget_session_expired_CFL)
				main_layout.add_widget(self.widget_notification_banner_CFL)
				main_layout.add_widget(self.widget_modal_overlay)
				main_layout.add_widget(self.widget_parent_menu_main_CFL)
				
				
				
				try:
					Logger.info("[CC LOG] Triggering a few functions on start-up...")
					self.hide_modal_overlay()
					self.update_layout_of_main_menu_home_button()
					self.generate_categories()
					Clock.schedule_once(self.set_inital_state_of_toggles, 1)
				except Exception as e:
					Logger.error(f"[CC LOG] Triggering of functions on start-up failed: {e}", exc_info=True)
				
				Logger.info("[CC LOG] Returning main layout!")
				return main_layout
		
		except Exception as e:
			Logger.error(f"[CC LOG] Failed to build the app: {e}", exc_info=True)
		
		
		
		
		''' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Start of FUNCTIONS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - '''
		
		
		
		
		try:
			def hide_modal_overlay(self, instance=None):
				print("FUNCTION 01e: Hide modal overlay and enable interaction with underlying widgets")
		
				self.widget_modal_overlay.opacity = 0.0
				self.widget_modal_overlay.disabled = False
	
	
	
			def show_modal_overlay(self, instance=None):
				print("FUNCTION 01f: Show modal overlay and disable interaction with underlying widgets")
		
				self.widget_modal_overlay.opacity = 0.1
				self.widget_modal_overlay.disabled = True
			
			
			
			def hide_register_page(self, instance=None):
				print("FUNCTION 02a: Hide register page")
		
				Animation(pos_hint={'x': 1, 'center_y': 0.5}, duration=0.0).start(self.widget_parent_page_register_CFL)
				self.widget_parent_body_CBL.disabled = False
		
				self.widget_label_reg_warning_CL.text = ""
				self.widget_textInput_regEmail.text = ""
				self.widget_textInput_regPassword.text = ""
				self.widget_textInput_regPwRepeat.text = ""
	
	
	
			def show_register_page(self, instance=None):
				print("FUNCTION 02b: Show register page")
		
				Animation(pos_hint={'x': 0, 'center_y': 0.5}, duration=0.0).start(self.widget_parent_page_register_CFL)
				self.widget_parent_body_CBL.disabled = True
				
				'''
				self.hide_all_other_pages(self.widget_parent_page_register_CFL)
				'''
			
			
			
			def hide_signIn_page(self, instance=None):
				print("FUNCTION 02c: Hide sign in page")
		
				Animation(pos_hint={'x': 1, 'center_y': 0.5}, duration=0.0).start(self.widget_parent_page_signIn_CFL)
				self.widget_parent_body_CBL.disabled = False
		
				self.widget_label_warning_signIn_CL.text = ""
				self.widget_textInput_entUsername.text = ""
				self.widget_textInput_entPassword.text = ""
				try:
					self.widget_parent_page_signIn_CFL.remove_widget(self.widget_user_email_CTI)
					self.widget_parent_page_signIn_CFL.remove_widget(self.widget_send_reset_link_CB)
					print("'Forgot password' widgets removed")
				except:
					print("No 'Forgot password' widgets to remove")
	
	
	
			def show_signIn_page(self, instance=None):
				print("FUNCTION 02d: Show sign in page")
		
				Animation(pos_hint={'x': 0, 'center_y': 0.5}, duration=0.0).start(self.widget_parent_page_signIn_CFL)
				self.widget_parent_body_CBL.disabled = True
				'''
				self.hide_all_other_pages(self.widget_parent_page_signIn_CFL)
				self.text_to_speech_stopped.set()
				self.stop_speech_recognition()	
				'''
			
			
			
			def hide_settings_page(self, instance=None):
				print("FUNCTION 02g: Hide settings page")
		
				Animation(pos_hint={'x': 1, 'center_y': 0.5}, duration=0.0).start(self.widget_parent_page_settings_CFL)
				self.widget_parent_body_CBL.disabled = False
		
				self.widget_label_save_set_warning_CL.color = (0.10, 0.70, 0.46, 1)
				self.widget_label_save_set_warning_CL.text = ""
	
	
	
			def show_settings_page(self, instance=None):
				print("FUNCTION 02h: Show settings page")
		
				Animation(pos_hint={'x': 0, 'center_y': 0.5}, duration=0.0).start(self.widget_parent_page_settings_CFL)
				self.widget_parent_body_CBL.disabled = True
				
				'''
				self.hide_all_other_pages(self.widget_parent_page_settings_CFL)
				self.text_to_speech_stopped.set()
				self.stop_speech_recognition()
				'''
			
			
			
			def hide_favorites_page(self, instance=None):
				print("FUNCTION 02i: Hide favorites page")
		
				Animation(pos_hint={'x': 1, 'center_y': 0.5}, duration=0.0).start(self.widget_parent_page_favorites_CFL)
				self.widget_parent_body_CBL.disabled = False
	
	
	
			def show_favorites_page(self, instance=None):
				print("FUNCTION 02j: Show favorites page")
		
				Animation(pos_hint={'x': 0, 'center_y': 0.5}, duration=0.0).start(self.widget_parent_page_favorites_CFL)
				self.widget_parent_body_CBL.disabled = True
				
				'''
				self.hide_all_other_pages(self.widget_parent_page_favorites_CFL)
				self.text_to_speech_stopped.set()
				self.stop_speech_recognition()		
				'''
			
			
			def hide_lab_page(self, instance=None):
				print("FUNCTION 02k: Hide laboratory page")
		
				Animation(pos_hint={'x': 1, 'center_y': 0.5}, duration=0.0).start(self.widget_parent_page_lab_CFL)
				self.widget_parent_body_CBL.disabled = False
	
	
	
			def show_lab_page(self, instance=None):
				print("FUNCTION 02l: Show laboratory page")
		
				Animation(pos_hint={'x': 0, 'center_y': 0.5}, duration=0.0).start(self.widget_parent_page_lab_CFL)
				self.widget_parent_body_CBL.disabled = True
		
				self.widget_label_warning_lab_CL.text = ""
				self.render_my_topics_list()
				'''
				self.hide_all_other_pages(self.widget_parent_page_lab_CFL)
				self.text_to_speech_stopped.set()
				self.stop_speech_recognition()
				'''
			
			
			
			def hide_main_menu(self, instance=None):
				print("FUNCTION 02o: Hide main menu")
		
				Animation(pos_hint={'x': -1, 'center_y': 0.5}, duration=0.3).start(self.widget_parent_menu_main_CFL)
	
	
	
			def show_main_menu(self, instance=None):
				print("FUNCTION 02p: Show main menu")
		
				Animation(pos_hint={'x': 0, 'center_y': 0.5}, duration=0.3).start(self.widget_parent_menu_main_CFL)
				
				'''
				self.text_to_speech_stopped.set()
				self.stop_speech_recognition()		
				'''
			
			
			
			def slide_register_page_right(self, instance=None):
				print("FUNCTION 03a: Slide register page right")
		
				Animation(pos_hint={'x': 0.75, 'center_y': 0.5}, duration=0.3).start(self.widget_parent_page_register_CFL)
	
	
	
			def slide_register_page_left(self, instance=None):
				print("FUNCTION 03b: Slide register page left")
		
				Animation(pos_hint={'x': 0, 'center_y': 0.5}, duration=0.3).start(self.widget_parent_page_register_CFL)
			
			
			
			def slide_signIn_page_right(self, instance=None):
				print("FUNCTION 03c: Slide sign in page right")
		
				Animation(pos_hint={'x': 0.75, 'center_y': 0.5}, duration=0.3).start(self.widget_parent_page_signIn_CFL)
	
	
	
			def slide_signIn_page_left(self, instance=None):
				print("FUNCTION 03d: Slide sign in page left")
		
				Animation(pos_hint={'x': 0, 'center_y': 0.5}, duration=0.3).start(self.widget_parent_page_signIn_CFL)
			
			
			
			def slide_settings_page_right(self, instance=None):
				print("FUNCTION 03g: Slide settings page right")
		
				Animation(pos_hint={'x': 0.75, 'center_y': 0.5}, duration=0.3).start(self.widget_parent_page_settings_CFL)
	
	
	
			def slide_settings_page_left(self, instance=None):
				print("FUNCTION 03h: Slide settings page left")
		
				Animation(pos_hint={'x': 0, 'center_y': 0.5}, duration=0.3).start(self.widget_parent_page_settings_CFL)
			
			
			
			def slide_favorites_page_right(self, instance=None):
				print("FUNCTION 03i: Slide favorites page right")
		
				Animation(pos_hint={'x': 0.75, 'center_y': 0.5}, duration=0.3).start(self.widget_parent_page_favorites_CFL)
	
	
	
			def slide_favorites_page_left(self, instance=None):
				print("FUNCTION 03j: Slide favorites page left")
		
				Animation(pos_hint={'x': 0, 'center_y': 0.5}, duration=0.3).start(self.widget_parent_page_favorites_CFL)
			
			
			
			def slide_lab_page_right(self, instance=None):
				print("FUNCTION 03k: Slide laboratory page right")
		
				Animation(pos_hint={'x': 0.75, 'center_y': 0.5}, duration=0.3).start(self.widget_parent_page_lab_CFL)
	
	
	
			def slide_lab_page_left(self, instance=None):
				print("FUNCTION 03l: Slide laboratory page left")
		
				Animation(pos_hint={'x': 0, 'center_y': 0.5}, duration=0.3).start(self.widget_parent_page_lab_CFL)
			
			
			
			def slide_widgets_right(self, instance=None):
				print("FUNCTION 03o: Slide widgets right")
		
				Animation(pos_hint={'center_x':1.25}, duration=0.3).start(self.widget_parent_menu_top_CBL)
				Animation(pos_hint={'center_x':1.25}, duration=0.3).start(self.widget_parent_body_CBL)
				Animation(pos_hint={'center_x':1.25}, duration=0.3).start(self.widget_parent_menu_bottom_CBL)
	
	
	
			def slide_widgets_left(self, instance=None):
				print("FUNCTION 03p: Slide widgets left")
		
				Animation(pos_hint={'center_x':0.5}, duration=0.3).start(self.widget_parent_menu_top_CBL)
				Animation(pos_hint={'center_x':0.5}, duration=0.3).start(self.widget_parent_body_CBL)
				Animation(pos_hint={'center_x':0.5}, duration=0.3).start(self.widget_parent_menu_bottom_CBL)
			
			
			
			def hide_notification_banner(self, instance=None):
				# print("FUNCTION 02q: Hide notification banner")
		
				Animation(pos_hint={'x': 1, 'center_y': 0.89}, duration=0).start(self.widget_notification_banner_CFL)
			
			
			
			def show_notification_banner(self, instance=None):
				print("FUNCTION 02r: Show notification banner")
		
				if instance != None and instance == "TTS and STT enabled?":
					if self.narration_enabled == False and self.silence_detection_enabled == False:
						self.widget_notification_banner_CL.text = "Narration and silence detection disabled in settings"
					elif self.narration_enabled == False and self.silence_detection_enabled == True:
						self.widget_notification_banner_CL.text = "Narration disabled in settings"
					elif self.narration_enabled == True and self.silence_detection_enabled == False:
						self.widget_notification_banner_CL.text = "Silence detection disabled in settings"
					else:
						self.widget_notification_banner_CL.text = ""
						return
			
					Animation(pos_hint={'x': 0, 'center_y': 0.89}, duration=0).start(self.widget_notification_banner_CFL)
					Clock.schedule_once(self.hide_notification_banner, 4)
			
			
			
			def slide_main_menu_and_toggle_modal_overlay(self, instance, touch):  # Detect touch events
				# print("FUNCTION 04a: Slide main menu and toggle modal overlay")
		
				# print(f"self:          {self}") # ConvoKeeper object
				# print(f"instance       {instance}") # Modal overlay object
				# print(f"Touch:         {touch}")
				if not self.widget_parent_menu_main_CFL.collide_point(*touch.pos): # Click outside menu area detected
			
					# print("Touch outside main menu")
					# First, hide the main menu if it is open
					if self.widget_parent_menu_main_CFL.x == 0: # If this condition is met it means that the main menu is open
						self.hide_main_menu()
						self.slide_widgets_left()
						
						# Hide pages
						if self.widget_parent_page_settings_CFL.x == self.widget_parent_page_settings_CFL.parent.width * 0.75: # If this condition is met it means that the settings page is open and slided to the right
							self.slide_settings_page_left()
						
						if self.widget_parent_page_signIn_CFL.x == self.widget_parent_page_signIn_CFL.parent.width * 0.75: # If this condition is met it means that the signIn page is open and slided to the right
							self.slide_signIn_page_left()
					
						if self.widget_parent_page_register_CFL.x == self.widget_parent_page_register_CFL.parent.width * 0.75: # If this condition is met it means that the signIn page is open and slided to the right
							self.slide_register_page_left()
				
						if self.widget_parent_page_favorites_CFL.x == self.widget_parent_page_favorites_CFL.parent.width * 0.75: # If this condition is met it means that the signIn page is open and slided to the right
							self.slide_favorites_page_left()
						
						
						if self.widget_parent_page_lab_CFL.x == self.widget_parent_page_lab_CFL.parent.width * 0.75: # If this condition is met it means that the signIn page is open and slided to the right
							self.slide_lab_page_left()
						'''
						if self.widget_parent_page_profile_CFL.x == self.widget_parent_page_profile_CFL.parent.width * 0.75: # If this condition is met it means that the profile page is open and slided to the right
							self.slide_profile_page_left()
				
						if self.widget_parent_page_support_CFL.x == self.widget_parent_page_support_CFL.parent.width * 0.75: # If this condition is met it means that the suppor page is open and slided to the right
							self.slide_support_page_left()
							'''
			
					# Second, deactivate the modal overlay if the main menu is already hidden
					elif self.widget_modal_overlay.disabled == True:
						self.hide_modal_overlay()
			
				else:
					print("Touch inside main menu")
		
				return False # Indicate that the touch event has NOT been handled
			
			
			
			def show_modal_overlay_AND_show_main_menu_AND_slide_widgets_right_AND_toggle_pages(self, instance):
				print("FUNCTION 04b: (COMBO) Show modal overlay AND show main menu AND slide wigets right AND toggle pages")
		
				self.show_modal_overlay()
				self.show_main_menu()
				self.slide_widgets_right()
		
				# Toggle pages
				if self.widget_parent_page_settings_CFL.x == 0: # If this condition is met it means that the page is showing and aligned to the left
					self.slide_settings_page_right()
				
				elif self.widget_parent_page_signIn_CFL.x == 0: # If this condition is met it means that the page is showing and aligned to the left
					self.slide_signIn_page_right()
				
				elif self.widget_parent_page_register_CFL.x == 0: # If this condition is met it means that the page is showing and aligned to the left
					self.slide_register_page_right()
				
				if self.widget_parent_page_favorites_CFL.x == 0: # If this condition is met it means that the page is showing and aligned to the left
					self.slide_favorites_page_right()
				
				if self.widget_parent_page_lab_CFL.x == 0: # If this condition is met it means that the page is showing and aligned to the left
					self.slide_lab_page_right()
				'''
				elif self.widget_parent_page_profile_CFL.x == 0: # If this condition is met it means that the page is showing and aligned to the left
					self.slide_profile_page_right()
		
				elif self.widget_parent_page_support_CFL.x == 0: # If this condition is met it means that the page is showing and aligned to the left
					self.slide_support_page_right()
					'''
			
			
			
			def hide_modal_overlay_AND_hide_main_menu_AND_slide_widgets_left_AND_toggle_pages(self, instance):
				print("FUNCTION 04c: (COMBO) Hide modal overlay AND hide main menu AND slide widgets left AND toggle pages")
		
				self.hide_modal_overlay()
				self.hide_main_menu()
				self.slide_widgets_left()
		
				# Toggle pages
				if instance == self.widget_button_mainMenuItem_home_CB or instance == self.widget_button_home_CB:
					# print("One of the HOME buttons pressed")
					self.hide_register_page()
					'''
					self.hide_profile_page()
					'''
					self.hide_favorites_page()
					self.hide_lab_page()
					self.hide_settings_page()
					'''
					self.hide_support_page()
					self.hide_signIn_page()
					'''

				elif instance == self.widget_button_mainMenuItem_settings_CB:
					# print("SETTINGS button in main menu pressed")
					self.widget_parent_page_settings_CFL.pos_hint={'x': 0.75, 'center_y': 0.5}
					self.slide_settings_page_left()
					self.hide_register_page()
					'''
					self.hide_profile_page()
					'''
					self.hide_favorites_page()
					self.hide_lab_page()
					# self.hide_settings_page()
					'''
					self.hide_support_page()
					'''
					self.hide_signIn_page()
			
				elif instance == self.widget_button_mainMenuItem_signInAndOut_CB:
					# print("Sign in button in main menu pressed")
					self.widget_parent_page_signIn_CFL.pos_hint={'x': 0.75, 'center_y': 0.5}
					self.slide_signIn_page_left()
			
					self.hide_register_page()
					self.hide_profile_page()
					self.hide_favorites_page()
					self.hide_lab_page()
					self.hide_settings_page()
					self.hide_support_page()
					# self.hide_signIn_page()
		
				elif instance == self.widget_button_mainMenuItem_favorites_CB:
					# print("Favorites button in main menu pressed")
					self.widget_parent_page_favorites_CFL.pos_hint={'x': 0.75, 'center_y': 0.5}
					self.slide_favorites_page_left()
					self.hide_register_page()
					'''
					self.hide_profile_page()
					# self.hide_favorites_page()
					'''
					self.hide_lab_page()
					self.hide_settings_page()
					'''
					self.hide_support_page()
					'''
					self.hide_signIn_page()
		
				elif instance == self.widget_button_mainMenuItem_lab_CB:
					# print("Laboratory button in main menu pressed")
					self.widget_parent_page_lab_CFL.pos_hint={'x': 0.75, 'center_y': 0.5}
					self.slide_lab_page_left()
					self.hide_register_page()
					'''
					self.hide_profile_page()
					'''
					self.hide_favorites_page()
					# self.hide_lab_page()
					self.hide_settings_page()
					'''
					self.hide_support_page()
					'''
					self.hide_signIn_page()
		
				elif instance == self.widget_button_mainMenuItem_support_CB:
					# print("Support button in main menu pressed")
					self.widget_parent_page_support_CFL.pos_hint={'x': 0.75, 'center_y': 0.5}
					self.slide_support_page_left()
			
					self.hide_register_page()
					'''
					self.hide_profile_page()
					'''
					self.hide_favorites_page()
					self.hide_lab_page()
					self.hide_settings_page()
					# self.hide_support_page()
					self.hide_signIn_page()
			
			
			
			def update_layout_of_main_menu_home_button(self, instance=None):
				print("FUNCTION 05a: Update layout of main menu HOME button")
		
				CustomButton.currently_pressed_button = self.widget_button_mainMenuItem_home_CB
				self.apply_layout_for_menu_buttons() 
	
	
	
			def update_layout_of_main_menu_settings_button(self, instance):
				print("FUNCTION 05b: Update layout of main menu SETTINGS button")
		
				CustomButton.currently_pressed_button = self.widget_button_mainMenuItem_settings_CB
				self.apply_layout_for_menu_buttons()
	
	
	
			def update_layout_of_main_menu_signIn_button(self, instance):
				print("FUNCTION 05c: Update layout of main menu SIGN IN / OUT button")
		
				CustomButton.currently_pressed_button = self.widget_button_mainMenuItem_signInAndOut_CB
				self.apply_layout_for_menu_buttons()
	
	
	
			def update_layout_of_main_menu_favorite_button(self, instance):
				print("FUNCTION 05d: Update layout of main menu FAVORITE button")
		
				CustomButton.currently_pressed_button = self.widget_button_mainMenuItem_favorites_CB
				self.apply_layout_for_menu_buttons()
	
	
	
			def update_layout_of_main_menu_lab_button(self, instance):
				print("FUNCTION 05e: Update layout of main menu LABORATORY button")
		
				CustomButton.currently_pressed_button = self.widget_button_mainMenuItem_lab_CB
				self.apply_layout_for_menu_buttons() 
			
			
			
			def apply_layout_for_standard_buttons(self, instance=None):
				# print("FUNCTION 06a: Apply layout for STANDARD button")
		
				if CustomButton.currently_pressed_button.button_type != 'Refresh':
					# print("The currently pressed button is NOT a category or menu button and NOT the refresh button!")
					CustomButton.currently_pressed_button.shape_bg_color.rgba = CustomButton.currently_pressed_button.background_color_normal
				else:
					if CustomButton.last_pressed_category_button == None:
						# print("The currently pressed button is the refresh button but NO category button was selected!")
						CustomButton.currently_pressed_button.shape_bg_color.rgba = CustomButton.currently_pressed_button.background_color_normal
					else:
						# print("The currently pressed button is the refresh button and a category button was selected!")
						CustomButton.currently_pressed_button.shape_bg_color.rgba = CustomButton.currently_pressed_button.background_color_normal
						CustomButton.last_pressed_category_button.shape_bg_color.rgba = CustomButton.last_pressed_category_button.background_color_normal
						CustomButton.last_pressed_category_button = None # Reset value of currently selected category button
			
			
			
			def apply_layout_for_category_buttons(self, instance=None):
				# print("FUNCTION 06b: Apply (updated) layout for CATEGORY button on main page")
		
				if CustomButton.last_pressed_category_button == None:
					# print("The currently pressed button is a category button but NO other category button is currently selected!")
					CustomButton.currently_pressed_button.shape_bg_color.rgba = CustomButton.currently_pressed_button.background_color_selected
					CustomButton.last_pressed_category_button = CustomButton.currently_pressed_button
		
				else:
					# print("The currently pressed button is a category button and another category button is currently selected!")
			
					if CustomButton.currently_pressed_button != CustomButton.last_pressed_category_button:
						# print("The previously selected category button is NOT the same as the currently selected category button")
						CustomButton.currently_pressed_button.shape_bg_color.rgba = CustomButton.currently_pressed_button.background_color_selected
						CustomButton.last_pressed_category_button.shape_bg_color.rgba = CustomButton.last_pressed_category_button.background_color_normal
						CustomButton.last_pressed_category_button = CustomButton.currently_pressed_button
					else:
						# print("The previously selected category button is the same as the currently selected category button")
						CustomButton.currently_pressed_button.shape_bg_color.rgba = CustomButton.currently_pressed_button.background_color_selected
						CustomButton.last_pressed_category_button = CustomButton.currently_pressed_button
	
	
	
			def apply_layout_for_menu_buttons(self, instance=None):
				# print("FUNCTION 06c: Apply (updated) layout for MAIN MENU buttons")
		
				# print("Menu button pressed!")
				if CustomButton.last_pressed_menu_button == None:
					# print("1: The currently pressed button is a menu button and NO other menu buttton is currently selected!")
					CustomButton.currently_pressed_button.line_bg_color.rgba = (0.83, 0.84, 0.85, 1)
			
					CustomButton.last_pressed_menu_button = CustomButton.currently_pressed_button
		
				else:
					# print("2: The currently pressed button is a menu button and another menu button is currently selected!")
			
					if CustomButton.currently_pressed_button != CustomButton.last_pressed_menu_button:
						# print("2a: The previously selected menu button is NOT the same as the currently selected menu button")
						CustomButton.last_pressed_menu_button.line_bg_color.rgba = (0, 0, 0, 0)
						CustomButton.currently_pressed_button.line_bg_color.rgba = (0.83, 0.84, 0.85, 1)
				
						CustomButton.last_pressed_menu_button = CustomButton.currently_pressed_button
					else:
						# print("2b: The previously selected menu button is the same as the currently selected menu button")
						CustomButton.currently_pressed_button.line_bg_color.rgba = (0.83, 0.84, 0.85, 1)
				
						CustomButton.last_pressed_menu_button = CustomButton.currently_pressed_button
			
			
			
			def check_session_token_validity(self):
				# print("FUNCTION 07a: Check session token validity")
				
				Logger.info("[CC LOG] Check session token validity function triggered")
				
				id_token = self.session_manager.get_id_token()
				Logger.info(f"[CC LOG] id_token: {id_token}")
				
				if id_token != None:
					if self.token_validator.validate_id_token(id_token):
						print("FUNCTION 07a: Check session token validity: Session token is valid")
						Logger.info("[CC LOG] Session token is valid")
						return True
			
					else:
						print("FUNCTION 07a: Check session token validity: Session token is NOT valid")
						Logger.info("[CC LOG] Session token is NOT valid")
						'''
						self.sign_user_out()
						'''
						return False
		
				else:
					print("FUNCTION 07a: Check session token validity: No session token stored")
					Logger.info("[CC LOG] No session token stored")
					return False
				
				id_token = None
				
				return False
			
			
			
			def close_session_expired_popup(self, instance):
				print("FUNCTION 07c: Close session expired popup")
		
				if instance.text == "To sign in page":
					Animation(pos_hint={'x': 1, 'center_y': 0.5}, duration=0.2).start(self.widget_session_expired_CFL)
					self.show_signIn_page()
					return True
				else:
					Animation(pos_hint={'x': 1, 'center_y': 0.5}, duration=0.2).start(self.widget_session_expired_CFL)
					self.hide_signIn_page()
					return True
			
			
			
			def generate_categories(self, instance=None, *args):
				print(f"FUNCTION 08a: Generate categories")
				
				Logger.info("[CC LOG] Generate categories function triggered")
		
				# print(f"self:                             {self}") # ConvoKeeper object
				# print(f"currently_pressed_button:         {CustomButton.currently_pressed_button}")
				# print(f"currently_pressed_button.text:    {CustomButton.currently_pressed_button.text}")
				# print(f"last_pressed_category_button:     {CustomButton.last_pressed_category_button}")
		
				# if CustomButton.last_pressed_category_button != None:
					# print(f"last_pressed_category_button.text {CustomButton.last_pressed_category_button.text}")
		
				self.selected_category = ""
				self.current_topic = ""
				self.all_categories = []
		
				for topicObject in all_topics:
					category = topicObject.get("category")
					if category not in self.all_categories:
						self.all_categories.append(category)
		
				random.shuffle(self.all_categories)
				
				if instance != None and instance.parent.parent != None and instance.parent.parent == self.widget_favorites_page_CBL:
					# print(f"instance.parent:     {instance.parent}") # Favorite category label (in favorites list) object
					# print(f"instance.parent.text:{instance.parent.text}")
					# print(f"instance:            {instance}") # Play button object
					# print(f"favorite_categories: {self.favorite_categories}")
					# print("")
					# print("One of the start buttons on the 'Favorites' page pressed")
					# print("")
					self.selected_category = instance.parent.text
					allCatsExceptSelected = [cat for cat in self.all_categories if cat != self.selected_category]
					threeCategoriesExtracted = allCatsExceptSelected[:3]
					self.generated_categories = [self.selected_category] + threeCategoriesExtracted
					self.update_category_buttons()
					self.generate_topic(instance)
					CustomButton.currently_pressed_button = self.widget_category_button_cat1_CB
					# CustomButton.last_pressed_category_button = self.widget_category_button_cat1_CB
					self.apply_layout_for_category_buttons()
		
				else:
					# print("The function was triggered by something else than one of the start buttons on the 'Favorites' page being pressed")
					# print("")
					self.generated_categories = self.all_categories[:4]
					self.update_category_buttons()
			
					# Reset current category, topic, start/skip button text and last (most recently) pressed category button
					self.selected_category = ""
					self.widget_label_topic_CL.text = f"{self.introtext}"
					self.widget_button_start_CB.text = "START"
					if CustomButton.last_pressed_category_button != None:
						CustomButton.last_pressed_category_button.shape_bg_color.rgba = CustomButton.last_pressed_category_button.background_color_normal
						CustomButton.last_pressed_category_button = None
			
			
			
			def update_category_buttons(self, instance=None):
				print(f"FUNCTION 08b: Update category buttons {self.generated_categories}")
				
				Logger.info("[CC LOG] Update category buttons function triggered")
				
				# Update button texts
				self.widget_category_button_cat1_CB.text = f"{self.generated_categories[0]}"
				self.widget_category_button_cat2_CB.text = f"{self.generated_categories[1]}"
				self.widget_category_button_cat3_CB.text = f"{self.generated_categories[2]}"
				self.widget_category_button_cat4_CB.text = f"{self.generated_categories[3]}"
		
				# Update favorite icon states
				'''
				if self.check_session_token_validity() == True:
					self.favorite_categories = self.fetch_favorite_categories(self.localId)
					'''
		
				self.set_favorite_icon_state(self.widget_category_button_cat1_CB)
				self.set_favorite_icon_state(self.widget_category_button_cat2_CB)
				self.set_favorite_icon_state(self.widget_category_button_cat3_CB)
				self.set_favorite_icon_state(self.widget_category_button_cat4_CB)
			
			
			
			def set_favorite_icon_state(self, instance=None):
				print("FUNCTION 08c: Set correct favorite icon state")
				
				Logger.info("[CC LOG] Set correct favorite icon state function triggered")
				
				# print(f"self:                {self}") # ConvoKeeper object
				# print(f"instance:            {instance}") # Category button object
				# print(f"instance.text:       {instance.text}")
				# print(f"favorite_categories: {self.favorite_categories}")
				for favorite_label in instance.children:
					# print(f"favorite_label:      {favorite_label} (text: {favorite_label.text}))")
					if self.favorite_categories != None:
						if instance.text in self.favorite_categories:
							# print("---> Category is a favorite! - - -")
							favorite_label.font_name = GLOBAL_FONT_UNICODE
							favorite_label.text = "\uf005"
							instance.is_favorite = True
						else:
							# print("---> Category is NOT a favorite - - -")
							favorite_label.font_name = "fonts/fa-regular-400"
							favorite_label.text = "\uf006"
							instance.is_favorite = False
			
			
			
			def generate_topic(self, instance):
				print("")
				print("FUNCTION 08d: Generate topic (category button pressed)")
		
				# print(f"self:                                {self}") # ConvoKeeper object
				# print(f"instance:                            {instance}") # Category button object in app body OR play button on favorites page
				# print(f"instance.text:                       {instance.text}")
		
				self.widget_button_start_CB.text = "START"
				if instance.parent == self.widget_category_buttons_CGL:
					self.selected_category = instance.text
				
				# print(f"Selected category:                   {self.selected_category}")
		
				if self.selected_category != "":
					self.topics_in_selected_category = []
					for topicObject in all_topics:
						if topicObject.get("category") == self.selected_category:
							topic = topicObject.get("topic")
							self.topics_in_selected_category.append(topic)
		   
					if self.topics_in_selected_category:
						random.shuffle(self.topics_in_selected_category)
						self.current_topic = self.topics_in_selected_category[0]
						# print(f"Current topic:                       {self.current_topic}")
						# print(f"Topics in selected category:")
						# print(f"{self.topics_in_selected_category}")
						# print("")

				else:
					print(f"No category selected, current topic: {self.current_topic}")
			
			
			
			def start_game(self, instance=None):
				print("")
				print("FUNCTION 08e: Start game (start/skip button pressed)")
		
				# print(f"self:                                {self}")
				# print(f"instance:                            {instance}") # Start/skip button object OR play button object
				# print(f"instance.text:                       {instance.text}")
				
				self.show_notification_banner("TTS and STT enabled?")
			
				if instance == None:
					# print("Function triggered automatically by monitoring function")
					random.shuffle(self.topics_in_selected_category)
					self.current_topic = self.topics_in_selected_category[0]
					self.widget_label_topic_CL.text = f"{self.current_topic}"
					#self.convert_text_to_speech()
					return
		
				if instance.text == "SKIP":
					# print("Skip button pressed, generating and showing new topic")
					random.shuffle(self.topics_in_selected_category)
					self.current_topic = self.topics_in_selected_category[0]
					self.widget_label_topic_CL.text = f"{self.current_topic}"
					#self.convert_text_to_speech()
		
				elif instance.text == "START" and self.current_topic != "":
					# print(f"Start button pressed, showing current topic")
					self.widget_label_topic_CL.text = f"{self.current_topic}"
					self.widget_button_start_CB.text = "SKIP"
					#self.convert_text_to_speech()
		
				elif instance.parent.parent == self.widget_favorites_page_CBL and self.current_topic != "":
					# print(f"Start button in favorite categories pressed, showing current topic")
					self.widget_label_topic_CL.text = f"{self.current_topic}"
					self.widget_button_start_CB.text = "SKIP"
					#self.convert_text_to_speech()
			
				else:
					# print(f"Start button pressed, but there is no current topic stored")
					self.widget_label_topic_CL.text = "Either there are no topics available for this category or no category has been selected."
			
			
			
			def set_inital_state_of_toggles(self, dt=None):
				print("FUNCTION 09c: Set intital state of toggles")
		
				if self.narration_enabled == True:
					self.toggle_button_tts_enabled_CB.state = 'normal'
				else:
					self.toggle_button_tts_enabled_CB.state = 'down'
		
				if self.silence_detection_enabled == True:
					self.toggle_button_sd_enabled_CB.state = 'normal'
				else:
					self.toggle_button_sd_enabled_CB.state = 'down'
		
				if self.agreed_to_TnCs_and_privacy_policy == "Yes":
					self.toggle_button_agree_CTB.state = 'normal'
				else:
					self.toggle_button_agree_CTB.state = 'down'
			
			
			
			def favorite_icon_pressed(self, instance, touch):
				if instance.collide_point(*touch.pos):
					print(f"FUNCTION 10a: (1) Favorite icon pressed")
			
					# print(f"self:                                 {self}") # ConvoKeeper object
					# print(f"instance.parent:                      {instance.parent}") # Category button object in app body
					# print(f"instance.parent.text:                 {instance.parent.text}")
					# print(f"instance.parent.is_favorite (before): {instance.parent.is_favorite}")
					# print(f"instance:                             {instance}") # Favorite icon label object
					# print(f"touch:                                {touch}")
					instance.parent.is_favorite = not instance.parent.is_favorite # Sets the value to the opposite of the current value
					# print(f"instance.parent.is_favorite (after):  {instance.parent.is_favorite}")
					self.add_or_remove_cat_as_favorite(instance.parent)
					return True  # Indicate the touch was handled
			
			
			
			def thrashcan_button_pressed(self, instance):
				print("FUNCTION 10a: (2) Trashcan button pressed")
		
				# print(f"self:                 {self}") # ConvoKeeper object
				# print(f"instance.parent:      {instance.parent}") # Favorite category label object
				# print(f"instance.parent.text: {instance.parent.text}") # Favorite category label object
				# print(f"instance:             {instance}") # Trashcan button object
		
				match_found = False
				for widget in self.root.walk():
					if isinstance(widget, CustomButton):
						if widget.button_type == 'Category':
							if widget.text == instance.parent.text:
								# print("Favorite removed found in app body")
								widget.is_favorite = not widget.is_favorite
								self.add_or_remove_cat_as_favorite(widget)
								self.render_favorites_list()
								match_found = True
								return True
		
				if match_found == False:
					# print("Favorite removed NOT found in app body")
					instance.parent.is_favorite = False
					self.add_or_remove_cat_as_favorite(instance.parent)
					self.render_favorites_list()
					return True
			
			
			
			def delete_topic_button_pressed(self, instance):
				print("FUNCTION 10a: (4) Delete topic button pressed")
		
				# print(f"self:                 {self}") # ConvoKeeper object
				# print(f"instance:             {instance}") # Category object
				# print(f"instance.text:        {instance.text}") # Category object
		
				match_found = False
				for widget in self.root.walk():
					if isinstance(widget, CustomButton):
						if widget.button_type == 'Category':
							if widget.text == instance.text:
								widget.is_favorite = False
								self.add_or_remove_cat_as_favorite(widget)
								match_found = True
								self.generate_categories()
								return True
		
				if match_found == False:
					# print("NOT found in app body")
					instance.is_favorite = False
					self.add_or_remove_cat_as_favorite(instance)
					self.generate_categories()
					return True
			
			
			
			def add_or_remove_cat_as_favorite(self, instance): # Triggered by function in the button class
				print("FUNCTION 10b: Add or remove category from favorite_categories and update favorite icon state")
		
				# print(f"self:             {self}") # ConvoKeeper object
				# print(f"instance.parent:  {instance.parent}") # Category grid object in app body OR Category box object on favorites page
				# print(f"instance:         {instance}") # Category button object in app body OR Category label object on favorites page
				# print(f"instance.text:    {instance.text}")
				# print(f"instance.is_favo: {instance.is_favorite}")
				# print(f"instance.children:{instance.children}") # Favorite icon label object OR play and trashcan button objects
		
				if instance.is_favorite == True: # 1
					# print(f" Category '{instance.text}' selected as favorite")
			
					# Update appearance of favourite icon label in app body
					if instance.parent != None and instance.parent == self.widget_category_buttons_CGL:
						instance.widget_favorite_label.font_name = GLOBAL_FONT_UNICODE
						instance.widget_favorite_label.text = "\uf005"
			
					# Store the selected category as favorite
					if self.check_session_token_validity() == True: # 5 
						try:
							# print("  User that selected the category as favorite is signed in")
							self.cursor.execute("SELECT category FROM favorites WHERE firebase_uid = ?", (self.localId,))
							currentFavoriteCategories = self.cursor.fetchone()
							# print(f"  Favorite categories (before add): {currentFavoriteCategories}")
					
							if any(any(char.isalpha() for char in item) for item in currentFavoriteCategories): # 6 
								# print("   User had other favorite categories stored")
								self.favorite_categories = json.loads(currentFavoriteCategories[0])
						
								if instance.text not in self.favorite_categories: # 7 
									# print(f"    Category {instance.text} was NOT in the list of stored favorite categories")
									self.favorite_categories.append(instance.text)
									self.favorite_categories_json = json.dumps(self.favorite_categories)
									self.cursor.execute("UPDATE favorites SET category = ? WHERE firebase_uid = ?",(self.favorite_categories_json, self.localId))
									self.conn.commit()
									# print(f"    Favorite categories (after add): {self.favorite_categories}")
								else: # 10
									print(f"    Category {instance.text} was in the list of stored favorite categories")
									# print(f"    Favorite categories (after add): {self.favorite_categories}")
					
							else: # 9
								# print("   User had NO other favorite categories stored")
								self.favorite_categories = [instance.text]
								self.favorite_categories_json = json.dumps(self.favorite_categories)
								self.cursor.execute("UPDATE favorites SET category = ? WHERE firebase_uid = ?",(self.favorite_categories_json, self.localId))
								self.conn.commit()
								# print(f"   Favorite categories (after add): {self.favorite_categories}")
				
						except:
							print("Failed to add category to favorites")
			
					else: # 2
						# print("  User that selected the category as favorite is NOT signed in")
						# print(f"  Favorite categories (before add): {self.favorite_categories}")
						self.favorite_categories.append(instance.text)
						print(f"  Favorite categories (after add): {self.favorite_categories}")
		
				else: # 3
					# print(f" Category '{instance.text}' de-selected as favorite")
			
					# Update appearance of favorite icon label in app body
					if instance.parent != None and instance.parent == self.widget_category_buttons_CGL:
						instance.widget_favorite_label.font_name = "fonts/fa-regular-400"	
						instance.widget_favorite_label.text = "\uf006"
						# print("Updated appearance of favorite icon label in app body")
			
					# Remove the selected category as favorite
					if self.check_session_token_validity() == True: # 8
						# print("  User that de-selected the category as favorite is signed in")
						try:
							self.cursor.execute("SELECT category FROM favorites WHERE firebase_uid = ?", (self.localId,))
							currentFavoriteCategories = self.cursor.fetchone()
							self.favorite_categories = json.loads(currentFavoriteCategories[0])
							# print(f"  Favorite categories (before remove): {self.favorite_categories}")
							self.favorite_categories.remove(instance.text)
							# print(f"  Favorite categories (after remove): {self.favorite_categories}")
							self.favorite_categories_json = json.dumps(self.favorite_categories)
							self.cursor.execute("UPDATE favorites SET category = ? WHERE firebase_uid = ?",(self.favorite_categories_json, self.localId))
							self.conn.commit()
				
						except:
							print("Failed to remove category from favorites")
					else: # 4
						# print("  User that de-selected the category as favorite is NOT signed in")
						# print(f"  Favorite categories (before remove): {self.favorite_categories}")
						self.favorite_categories.remove(instance.text)
						print(f"  Favorite categories (after remove): {self.favorite_categories}")
			
			
			
			def render_favorites_list(self, instance=None):
				print("FUNCTION 10c: Render favorites list on favorites page")
		
				# print(f"self.favorite_categories: {self.favorite_categories}")
				self.favorite_categories_count = len(self.favorite_categories)
				# print(f"favorite_categories_count: {self.favorite_categories_count}")
		
				self.widget_favorites_page_CBL.clear_widgets()
		
				if len(self.favorite_categories) >= 1:
					for item in self.favorite_categories:
						widget_favorite_category_CL =        CustomLabel(app_ref=self,  text=f"{item}", color=(0.15, 0.16, 0.18, 1), font_size=34, background_color=(1, 0.85, 0.2, 1), font_name=GLOBAL_FONT_BOLD, pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(0.7, None), shape_type="rectangle_rounded", label_type="Favorite category", corner_radius=30)
						widget_favorite_category_start_CB =  CustomButton(app_ref=self, text="\uf144",  color=(0.15, 0.16, 0.18, 1), font_size=38, font_name=GLOBAL_FONT_UNICODE, pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(None, None), background_color_flicker=(0, 0, 0, 0))
						widget_favorite_category_remove_CB = CustomButton(app_ref=self, text="\uF1F8",  color=(0.15, 0.16, 0.18, 1), font_size=32, font_name=GLOBAL_FONT_UNICODE, pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(None, None), background_color_flicker=(0, 0, 0, 0))
				
						widget_favorite_category_start_CB.bind(on_release=self.start_game)
						widget_favorite_category_start_CB.bind(on_release=self.generate_categories)
						widget_favorite_category_start_CB.bind(on_release=self.hide_favorites_page)
						widget_favorite_category_remove_CB.bind(on_release=self.thrashcan_button_pressed)
				
						widget_favorite_category_CL.add_widget(widget_favorite_category_start_CB)
						widget_favorite_category_CL.add_widget(widget_favorite_category_remove_CB)
						self.widget_favorites_page_CBL.add_widget(widget_favorite_category_CL)
		
				else:
					widget_no_favorite_category_CL = CustomLabel(app_ref=self, text="No favorite categories selected", color=(1, 1, 1, 1), font_name=GLOBAL_FONT_BOLD, pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(1, None), shape_type="rectangle_rounded", corner_radius=30)
					self.widget_favorites_page_CBL.add_widget(widget_no_favorite_category_CL)
		
				# Clock.schedule_once(self.reset_font_size_after_list_rendered, 0.05)
			
			
			
			def create_topic(self, instance):
				print("FUNCTION 11a: Create topic")
		
				self.widget_label_warning_lab_CL.text = ""
				new_category = self.widget_textInput_category_CTI.text
				new_topic = self.widget_textInput_topic_CTI.text
				topic_creation_regex = r'^[^{}\[\]:,"\\]+$'
		
				if self.check_session_token_validity() == False:
					self.widget_label_warning_lab_CL.color = (1, 0, 0, 1)
					self.widget_label_warning_lab_CL.text = "You must be signed in to create topics"
					return
			
				if len(new_category) <= 0 or len(new_topic) <= 3:
					self.widget_label_warning_lab_CL.color = (1, 0, 0, 1)
					self.widget_label_warning_lab_CL.text = "Incorrect category or topic"
					return
		
				if len(new_topic) >= 76:
					self.widget_label_warning_lab_CL.color = (1, 0, 0, 1)
					self.widget_label_warning_lab_CL.text = f"Topic exceeds max length ({len(new_topic)} > 75)"
					return
		
				if not re.match(topic_creation_regex, new_category):
					self.widget_label_warning_lab_CL.color = (1, 0, 0, 1)
					self.widget_label_warning_lab_CL.text = f"Category contains illegal characters"
					return
		
				if not re.match(topic_creation_regex, new_topic):
					self.widget_label_warning_lab_CL.color = (1, 0, 0, 1)
					self.widget_label_warning_lab_CL.text = f"Topic contains illegal characters"
					return
				
				for topicObject in all_topics:
					if topicObject.get("topic") == new_topic:
						self.widget_label_warning_lab_CL.color = (1, 0, 0, 1)
						categoryy = topicObject.get("category")
						self.widget_label_warning_lab_CL.text = f"Topic already exists in cat: {categoryy}"
						return
		
				new_topic = {
					"category": new_category,
					"topic": new_topic,
					"creator": self.localId,
					"approved": "False"
				}
		
				all_topics.append(new_topic)
				file_path = "topics.py"
				with open(file_path, "w") as f:
					f.write("all_topics = ")
					f.write(json.dumps(all_topics, indent=4))
			
					myCategoryLabel = CustomLabel(text=f"{new_category}")
					self.create_topic_button_pressed(myCategoryLabel)
					self.widget_label_warning_lab_CL.color = (0.10, 0.70, 0.46, 1)
					self.widget_label_warning_lab_CL.text = "Topic created and category added to favorites"
					self.render_my_topics_list()
			
					# Clear inputs
					self.widget_textInput_category_CTI.text = ""
					self.widget_textInput_topic_CTI.text = ""
	
	
	
			def delete_topic(self, instance):
				print("FUNCTION 11b: Delete topic")
		
				self.widget_label_warning_lab_CL.text = ""
				del_topic = instance.parent.text
				print(f"del_topic: {del_topic}")
		
				for topicObject in all_topics:
					if topicObject.get("topic") == del_topic and topicObject.get("creator") == self.localId:
						del_category = topicObject.get("category")
						all_topics.remove(topicObject)
						file_path = "topics.py"
						with open(file_path, "w") as f:
							f.write("all_topics = ")
							f.write(json.dumps(all_topics, indent=4))
							print("Topic deleted:")
							print(f"{topicObject}")
					
							myCategoryLabel = CustomLabel(text=f"{del_category}")
							self.delete_topic_button_pressed(myCategoryLabel)
							self.widget_label_warning_lab_CL.color = (1, 0, 0, 1)
							self.widget_label_warning_lab_CL.text = "Topic deleted and removed from favorites"    
							self.render_my_topics_list()
	
	
	
			def render_my_topics_list(self, instance=None):
				print("FUNCTION 11c: Render my topics list")
		
				if self.check_session_token_validity() == True:
					self.widget_label_note_lab_CL.text = ""
				else:
					self.widget_label_note_lab_CL.text = "(feature only available for signed in users)"
		
				has_favorites = False
				scrollable_content = CustomBoxLayout(orientation="vertical", size_hint=(1, None), shape_type="rectangle")
				scrollable_content.bind(minimum_height=scrollable_content.setter('height'))
				my_categories = []
		
				if self.widget_labResults_CFL.children != None:
					self.widget_labResults_CFL.clear_widgets()
		
				if self.widget_labResults_SV.children != None:
					self.widget_labResults_SV.clear_widgets()
		
				if scrollable_content.children != None:
					scrollable_content.clear_widgets()
		
				myTopicsHeaderLabel = CustomLabel(app_ref=self, text="My topics", size_hint_y=None, height=40, halign="center", font_name=GLOBAL_FONT_BOLD)
				scrollable_content.add_widget(myTopicsHeaderLabel)
		
				for topicObject in all_topics:
					if topicObject.get("creator") == self.localId:
						topic = topicObject.get("topic")
						myTopicLabel =  CustomLabel(app_ref=self,  text=f"{topic}", size_hint_y=None, height=100, font_size=32, halign="center", padding=[30, 0, 30, 0])
						deleteMyTopic = CustomButton(app_ref=self, text="\uF1F8",  size_hint=(None, None), size=(28, 28), font_size=28, halign="right", font_name=GLOBAL_FONT_UNICODE)
						deleteMyTopic.bind(on_release=self.delete_topic)
						myTopicLabel.add_widget(deleteMyTopic)
						scrollable_content.add_widget(myTopicLabel)
						has_favorites = True
		
				if has_favorites == True:
					self.widget_labResults_SV.add_widget(scrollable_content)
					self.widget_labResults_CFL.add_widget(self.widget_labResults_SV)
			
					Clock.schedule_once(self.fix_del_topic_button_pos, 0.2)
		
				else:
					print("User has NO created topics")
	
	
	
			def fix_del_topic_button_pos(self, instance):
				print("FUNCTION 11d: Fix delete topic button positioning")
		
				for ScrollView in self.widget_labResults_CFL.children:
					for CustomBoxLayout in ScrollView.children:
						for label in CustomBoxLayout.children:
							if label.children != None:
								for button in label.children:
									button.x = label.x + label.width - button.width - 2
									button.y = label.y + label.font_size + 4
			
			
			
			def sign_in_profile_button_pushed(self, instance=None):
				print("FUNCTION 12a: Show sign in page or profile page")
		
				if self.check_session_token_validity() == True:
					self.show_profile_page()
					# print("12c.1: Showing profile page since user is logged in!")
				else:
					self.show_signIn_page()
					# print("12c.2: Showing sign in page since user is logged out")
			
			
			
			def register_user(self, instance):
				print("FUNCTION 13a: Register user")
				
				Logger.info(f"[CC LOG] Register user function triggered")	
		
				self.widget_label_reg_warning_CL.text = ""
		
				if self.agreed_to_TnCs_and_privacy_policy == "No":
					self.widget_label_reg_warning_CL.color = (1, 0, 0, 1)
					self.widget_label_reg_warning_CL.text = "Please agree to T&Cs and Privacy Policy to register user"
					return
		
				email_registered = self.widget_textInput_regEmail.text
				password_registered = self.widget_textInput_regPassword.text
		
				if self.check_internet_connection() == True:
					if email_registered != "" and password_registered != "":
						if password_registered == self.widget_textInput_regPwRepeat.text:
							requestSent = False
							try:
								payload_reg = {
									"email": email_registered,
									"password": password_registered,
									"returnSecureToken": True
								}
						
								firebase_signUp_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_KEY}"
								registerUserResponse = requests.post(firebase_signUp_url, json=payload_reg)
								requestSent = True
					
							except:
								self.widget_label_reg_warning_CL.color = (1, 0, 0, 1)
								self.widget_label_reg_warning_CL.text = "Error trying to register user"
								requestSent = False
								Logger.error(f"[CC LOG] Error trying to register user: {e}", exc_info=True)
					
							email_registered = None
							password_registered = None
						
							if requestSent == True:
								if registerUserResponse.status_code == 200:
									registerUserResponseJSON = registerUserResponse.json()
									localId = registerUserResponseJSON.get("localId")
									email = registerUserResponseJSON.get("email")
									idToken = registerUserResponseJSON.get("idToken")
							
									print("")
									print(f"localId: {localId}")
									print("")
							
									self.widget_label_reg_warning_CL.color = (0.10, 0.70, 0.46, 1)
									self.widget_label_reg_warning_CL.text = "User registered succesfully"
							
									# Store user locally
									self.store_user_locally(localId, email)
							
									# Send e-mail verification e-mail
									if self.email_verification_email_sent(idToken) == True:
										print("User registered but remains to verify e-mail address")
										self.show_signIn_page()
										self.widget_label_warning_signIn_CL.text = "Check e-mail to finalize registration"
										self.widget_textInput_entUsername.text = email
										'''
										self.update_sign_in_out_button()
										self.update_sign_in_profile_button()
										'''
										Logger.info(f"[CC LOG] User registered but remains to verify e-mail address")
							
									else:
										self.widget_label_reg_warning_CL.color = (1, 0, 0, 1)
										self.widget_label_reg_warning_CL.text = "Error sending registration e-mail"
										Logger.error(f"[CC LOG] Error sending registration e-mail: {e}", exc_info=True)
							
									registerUserResponseJSON = None
									localId = None
									email = None
									idToken = None	
						
								else:
									registerUserResponseJSON = registerUserResponse.json()
									error = registerUserResponseJSON.get("error")
									code = error.get("code")
									message = error.get("message")
							
									print("Failed to register user")
									self.widget_label_reg_warning_CL.color = (1, 0, 0, 1)
									self.widget_label_reg_warning_CL.text = f"{code}: {message}"
						
						else:
							self.widget_label_reg_warning_CL.color = (1, 0, 0, 1)
							self.widget_label_reg_warning_CL.text = "Passwords entered do not match"
			
					else:
						self.widget_label_reg_warning_CL.color = (1, 0, 0, 1)
						self.widget_label_reg_warning_CL.text = "All fields must be filled in"
		
				else:
					self.widget_label_reg_warning_CL.color = (1, 0, 0, 1)
					self.widget_label_reg_warning_CL.text = "Check internet connection"
			
			
			
			
			def store_user_locally(self, localId, email):
				print("FUNCTION 13b: Store user in local database")
		
				try:
					self.cursor.execute("INSERT INTO users (firebase_uid, email, agreed_to_TnCs_and_PP) VALUES (?, ?, ?)", (localId, email, self.agreed_to_TnCs_and_privacy_policy))
					self.conn.commit()
					print("Successfully created users table in local DB")
		
				except:
					print("Failed to create users table in local DB")
		
				try:
					initiate_favorite_categories_json = json.dumps([])
					self.cursor.execute("INSERT INTO favorites (firebase_uid, category) VALUES (?, ?)",(localId, initiate_favorite_categories_json))
					self.conn.commit()
					print("Successfully created favorites table in local DB")
		
				except:
					print("Failed to create favorites table in local DB")
		
				try:
					self.cursor.execute("INSERT INTO settings (firebase_uid, narration_enabled, silence_detection_enabled, voice_recognition_language, awkward_silence_limit, background_noise_calibration) VALUES (?, ?, ?, ?, ?, ?)", (localId, self.narration_enabled, self.silence_detection_enabled, self.voice_recognition_language, self.awkward_silence_limit, self.background_noise_calibration))
					self.conn.commit()
					print("Successfully created settings table in local DB")
		
				except:
					print("Failed to create settings table in local DB")
	
	
	
			def email_verification_email_sent(self, idToken):
				print("FUNCTION 13c: Send e-mail verification e-mail")
		
				requestSent = False
				try:
					payload_verEmail = {
						"requestType": "VERIFY_EMAIL",
						"idToken": idToken
					}
			
					firebase_sendOobCode_url = f"https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key={FIREBASE_KEY}"
					sendVerificationEmailResponse = requests.post(firebase_sendOobCode_url, json=payload_verEmail)
					requestSent = True
			
				except:
					requestSent = False
		
				if requestSent == True:
					if sendVerificationEmailResponse.status_code == 200:
						print("Verification e-mail sent succesfully")
						return True
					else:
						print("Failed to send verification e-mail")
						return False
				else:
					print("Error trying to send verification e-mail")
					return False
	
	
	
			def update_email_address(self, email_new):
				print("FUNCTION 13d: Update e-mail address")
		
				id_token = self.session_manager.get_id_token()
				requestSent = False
		
				try:
					payload_updEmail = {
						"requestType": "VERIFY_AND_CHANGE_EMAIL",
						"idToken": id_token,
						"new_email": email_new
					}
			
					firebase_updateEmail_url = f"https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key={FIREBASE_KEY}"
					updateEmailResponse = requests.post(firebase_updateEmail_url, json=payload_updEmail)
					requestSent = True
			
				except:
					requestSent = False
		
				if requestSent == True:
					if updateEmailResponse.status_code == 200:
						print("Verification e-mail sent succesfully")
						return True
					else:
						print("Failed to send verification e-mail")
						return False
				else:
					print("Error trying to send verification e-mail")
					return False
		
				id_token = None
			
			
			
			
			def sign_in(self, instance):
				print("FUNCTION 14a: Sign in")
				
				Logger.info("[CC LOG] Sign in function triggered")
				
				self.widget_label_warning_signIn_CL.text = ""
		
				email_entered = self.widget_textInput_entUsername.text
				password_entered = self.widget_textInput_entPassword.text
				attempts = self.rate_limiter.attempts_made(email_entered)
				
				if self.check_internet_connection() == True:
					if self.rate_limiter.is_allowed(email_entered):
						requestSent = False
						try:
							payload_signIn = {
								"email": email_entered,
								"password": password_entered,
								"returnSecureToken": True
							}
					
							firebase_signIn_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_KEY}"
							signUserInResponse = requests.post(firebase_signIn_url, json=payload_signIn)
							requestSent = True
							Logger.info("[CC LOG] Sign in API request was successful")
					
						except Exception as e:
							self.widget_label_warning_signIn_CL.text = "Error trying to sign user in"
							Logger.error("[CC LOG] Sign in API request failed: {e}")
							requestSent = False
					
						if requestSent == True:
							if signUserInResponse.status_code == 200:
								signUserInResponseJSON = signUserInResponse.json()
								idToken = signUserInResponseJSON.get("idToken")
								localId = signUserInResponseJSON.get("localId")
						
								if self.verify_account_activated(idToken, localId) == True:
									self.session_manager.set_id_token(idToken)
									self.localId = localId
									
									self.favorite_categories = self.fetch_favorite_categories(localId)
									self.fetch_settings(localId)
									self.hide_signIn_page()
									self.hide_register_page()
									'''
									self.update_sign_in_out_button()
									self.update_sign_in_profile_button()
									'''
									
									self.generate_categories()
									self.rate_limiter.reset(email_entered)
							
							
									print("+ + + Access granted + + +")
									Logger.info("[CC LOG] Sign in was successful!")
						
								else:
									print("- - - Access denied - - -")
									self.widget_label_warning_signIn_CL.text = "Account not activated"
									Logger.info("[CC LOG] Account not activated")
						
								signUserInResponseJSON = None
								idToken = None
								localId = None
					
							else:
								print("- - - Access denied - - -")
								signUserInResponseJSON = signUserInResponse.json()
								error = signUserInResponseJSON.get("error")
								code = error.get("code")
								message = error.get("message")
								self.widget_label_warning_signIn_CL.text = f"{code}: {message}"
								Logger.error(f"[CC LOG] Sign in attempt failed: {message}")
				
						email_entered = None
						password_entered = None
			
					else:
						print("- - - Access denied - - -")
						self.widget_label_warning_signIn_CL.text = f"Max attempts per {self.rate_limiter.period} seconds reached ({attempts}/{self.rate_limiter.limit})"
						Logger.info("[CC LOG] Sign in attempt failed, too many attempts")
				else:
					self.widget_label_warning_signIn_CL.text = "Check internet connection"
					Logger.info("[CC LOG] Sign in attempt failed, check internet connection")
	
	
	
			def verify_account_activated(self, idToken, localId):
				print("FUNCTION 14b: Verify account activated")
				
				Logger.info("[CC LOG] Verify account activated function triggered")
				
				sync_status_stored = 0
		
				try:
					self.cursor.execute("SELECT sync_status FROM users WHERE firebase_uid = ?", (localId,))
					sync_status_fetched = self.cursor.fetchone()
					sync_status_stored = sync_status_fetched[0]
					Logger.info("[CC LOG] Account activation status fetched successfully from DB")
		
				except:
					print("Failed to fetch account activation status from DB")
					Logger.error("[CC LOG] Failed to fetch account activation status from DB")
		
				if sync_status_stored == 0:
					try:
						payload_syncStatus = {
							"idToken": idToken
						}
				
						firebase_syncStatus_url = f"https://identitytoolkit.googleapis.com/v1/accounts:lookup?key={FIREBASE_KEY}"
						accountActivatedResponse = requests.post(firebase_syncStatus_url, json=payload_syncStatus)
				
						if accountActivatedResponse.status_code == 200:
							accountActivatedResponseJSON = accountActivatedResponse.json()
							users = accountActivatedResponseJSON.get("users")
							for user in users:
								emailVerified = user.get("emailVerified")
						
								if emailVerified == True:
									print("Account activated in Firebase but not in local DB")
									Logger.info("[CC LOG] Account activated in Firebase but not in local DB")
							
									#Store status in DB
									try:
										self.cursor.execute("UPDATE users SET sync_status = ? WHERE firebase_uid = ?", (1, localId))
										self.conn.commit()
										print("Sync status stored in local DB")
										Logger.info("[CC LOG] Sync status stored in local DB")
									except:
										print("Failed to store sync status in local DB")
										Logger.error("[CC LOG] Failed to store sync status in local DB")
									return True
						
								else:
									Logger.info("[CC LOG] E-mail not verified")
									return False
						
								accountActivatedResponseJSON = None
								users = None
								emailVerified = None
				
						else:
							print("Error in sync status API call")
							Logger.error("[CC LOG] Error in sync status API call")
							return False
			
					except:
						print("Failed to fetch account activation status from Firebase")
						Logger.error("[CC LOG] Failed to fetch account activation status Firebase")
						return False
			
				else:
					print("Account activated in local DB")
					Logger.info("[CC LOG] Account activated in local DB")
					return True
	
	
		
			def fetch_favorite_categories(self, localId):
				print("FUNCTION 14c: Fetch favorite categories")
		
				try:
					self.cursor.execute("SELECT category FROM favorites WHERE firebase_uid = ?", (localId,))
					favCatsFetchedFromDBjson = self.cursor.fetchone()
					favCatsFetchedFromDB = json.loads(favCatsFetchedFromDBjson[0])
					
					Logger.info("[CC LOG] Favorite categories fetched from local DB")
			
					return favCatsFetchedFromDB
		
				except:
					self.widget_label_warning_signIn_CL.text = "Failed to fetch favorite categories"
					print("Failed to fetch favorite categories")
					Logger.error("[CC LOG] Failed to fetch favorite categories from local DB")
	
	
	
			def fetch_settings(self, localId):
				print("FUNCTION 14d: Fetch settings")

				try:
					self.cursor.execute("""
						SELECT 
							narration_enabled, 
							silence_detection_enabled, 
							awkward_silence_limit, 
							voice_recognition_language, 
							background_noise_calibration 
						FROM settings 
						WHERE firebase_uid = ?
					""", (localId,))
					result = self.cursor.fetchone()

					if result:
						if result[0] == "1":
							self.narration_enabled = True
						else:
							self.narration_enabled = False
						if result[1] == "1":
							self.silence_detection_enabled = True
						else:
							self.silence_detection_enabled = False
						self.awkward_silence_limit = result[2]
						self.voice_recognition_language = result[3]
						self.background_noise_calibration = result[4]
				
						# Reload settings widgets
						self.toggle_button_tts_enabled_CB.state = 'normal' if self.narration_enabled else 'down'
						self.toggle_button_sd_enabled_CB.state = 'normal' if self.silence_detection_enabled else 'down'
						self.spinner_vr_language_SP.text = self.voice_recognition_language
						self.slider_max_silence_SL.value = self.awkward_silence_limit
						self.slider_bg_noise_cal_SL.value = self.background_noise_calibration
						
						Logger.info("[CC LOG] Settings fetched from local DB")
			
					else:
						print("No settings found for the user")
						Logger.error("[CC LOG] No settings found for the user")

				except:
					print(f"Failed to fetch settings")
					Logger.error("[CC LOG] Failed to fetch settings from local DB")
			
			
			
			def save_settings(self, instance):
				print("FUNCTION 16b: Save settings")
		
				self.widget_label_save_set_warning_CL.text = ""
		
				if self.check_session_token_validity() == True:
					try:
						self.cursor.execute("UPDATE settings SET narration_enabled = ? WHERE firebase_uid = ?", (self.narration_enabled, self.localId))
						self.cursor.execute("UPDATE settings SET silence_detection_enabled = ? WHERE firebase_uid = ?", (self.silence_detection_enabled, self.localId))
						self.cursor.execute("UPDATE settings SET awkward_silence_limit = ? WHERE firebase_uid = ?", (self.awkward_silence_limit, self.localId))
						self.cursor.execute("UPDATE settings SET voice_recognition_language = ? WHERE firebase_uid = ?", (self.voice_recognition_language, self.localId))
						self.cursor.execute("UPDATE settings SET background_noise_calibration = ? WHERE firebase_uid = ?", (self.background_noise_calibration, self.localId))
						self.conn.commit()
				
						self.widget_label_save_set_warning_CL.color = (0.10, 0.70, 0.46, 1)
						self.widget_label_save_set_warning_CL.text = "Settings saved successfully"
					except:
						self.widget_label_save_set_warning_CL.color = (1, 0, 0, 1)
						self.widget_label_save_set_warning_CL.text = "Failed to save settings"
				else:
					self.widget_label_save_set_warning_CL.color = (1, 0, 0, 1)
					self.widget_label_save_set_warning_CL.text = "Must be signed in to save settings"
			
			
			
			def toggle_button_toggled(self, instance):
				print(f"FUNCTION 18a: Toggle button toggled")
		
				if instance.state == 'normal': # ENABLE
					if instance.toggle_name == "Narration enabled":
						self.narration_enabled = True
						print("Narration enabled!")
				
					elif instance.toggle_name == "Silence detection enabled":
						self.silence_detection_enabled = True
						print("Silence detection enabled!")
			
					elif instance.toggle_name == "Agreed to T&C and PP":
						self.agreed_to_TnCs_and_privacy_policy = "Yes"
						print("User agreed to T&Cs and Privacy Policy")
				
				elif instance.state == 'down': # DISABLE
					if instance.toggle_name == "Narration enabled":
						self.narration_enabled = False
						print("Narration disabled..")
				
					elif instance.toggle_name == "Silence detection enabled":
						self.silence_detection_enabled = False
						print("Silence detection disabled..")
			
					elif instance.toggle_name == "Agreed to T&C and PP":
						self.agreed_to_TnCs_and_privacy_policy = "No"
						print("User did NOT agree to T&Cs and Privacy Policy")
			
	
	
			def slider_button_slided(self, instance, value):
				# print(f"FUNCTION 18b: Slider button slided")
		
				rounded_value = round(instance.value)
		
				if instance == self.slider_max_silence_SL:
					self.slider_max_silence_SL.value = rounded_value
					self.awkward_silence_limit = rounded_value
					self.widget_label_max_silence_CL.text = f"Awkward silence limit ({self.awkward_silence_limit} s):"
		
				elif instance == self.slider_bg_noise_cal_SL:
					self.slider_bg_noise_cal_SL.value = rounded_value
					self.background_noise_calibration = rounded_value
					self.widget_label_bg_noise_cal_CL.text = f"Background noise calibration ({self.background_noise_calibration}):"
	   
		
		
			def spinner_button_spinned(self, instance, text):
				print(f"FUNCTION 18c: Spinner button spinned")
		
				self.voice_recognition_language = instance.text
	
	
	
			def check_internet_connection(self):
				# print(f"FUNCTION XXX: Check internet connection")
		
				try:
					context = ssl._create_unverified_context()
					urllib.request.urlopen("https://www.google.com", timeout=4, context=context)
					# print("FUNCTION XXX: Check internet connection: Internet connection detected")
					Logger.info("[CC LOG] Internet connection detected!")
					return True
				
				except urllib.error.URLError as e:
					# print("FUNCTION XXX: Check internet connection: No internet connection detected")
					Logger.info(f"[CC LOG] NO internet connection detected (url error): {e}")
					return False
				
				except Exception as e:
					# print("FUNCTION XXX: Check internet connection: No internet connection detected")
					Logger.info(f"[CC LOG] NO internet connection detected (unexpected error): {e}")
					return False
			
			
			
			def open_url(self, instance, ref):
				print("FUNCTION YYY: Open URL")
		
				if self.check_internet_connection() == True:
					if ref == "jira_issue_link":
						webbrowser.open(self.jiraIssueLink)
					elif ref == "T&Cs":
						webbrowser.open("https://crappcompany.com/convokeeper/terms_and_conditions")
					elif ref == "PP":
						webbrowser.open("https://crappcompany.com/convokeeper/privacy_policy")
					elif ref == "support":
						webbrowser.open("mailto:support@support@crappcompany.com")
				else:
					print("No internet dude")
			
			
			
			Logger.info("[CC LOG] All functions loaded successfully!")
						
		except Exception as e:
			Logger.error(f"[CC LOG] One of the functions failed: {e}", exc_info=True)


	
	if __name__ == "__main__":
		Logger.info("[CC LOG] Calling the app class...")
		ConvoKeeper().run()

except Exception as e:
	Logger.error(f"[CC LOG] Failed to start app: {e}", exc_info=True)
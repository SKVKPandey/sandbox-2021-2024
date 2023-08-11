from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, firestore, storage

app = Flask(__name__)

# Step 2: Initialize the Firebase Admin SDK with your service account key and storage bucket
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {'storageBucket': 'esoapp-417e0.appspot.com'})


def upload_image_to_storage(file):
    # Get the Firebase Storage bucket
    bucket = storage.bucket()

    # Get the file name and file content from the Flask request object
    filename = file.filename
    file_content = file.read()

    # Create a new blob (file) in the bucket
    blob = bucket.blob(filename)

    # Upload the file content to the blob
    blob.upload_from_string(file_content, content_type=file.content_type)

    # Get the public URL of the uploaded file
    blob.make_public()
    file_url = blob.public_url

    return file_url

@app.route('/', methods=['GET', 'POST'])
def upload_data():
    if request.method == 'POST':
        if 'flyer' in request.files:
            # Process course data upload
            flyer = request.files['flyer']
            flyer_url = upload_image_to_storage(flyer)

            # Get other form data for courses
            course_name = request.form['course_name']
            background_image = request.files['background-image']
            background_image_url = upload_image_to_storage(background_image)
            detailed_description = request.form['detailed_description']
            short_description = request.form['short_description']
            key_highlights = request.form['key_highlights']
            duration = request.form['duration']
            pre_requisite = request.form['pre_requisite']
            amount = request.form['amount']

            # Rest of the instructor details
            instructors_image = background_image = request.files['instructor-image']
            instructors_image_url = upload_image_to_storage(instructors_image)
            instructors_name = request.form['instructors_name']
            bio = request.form['bio']
            linkedin_handle = request.form['linkedin_handle']
            instagram_handle = request.form['instagram_handle']
            twitter_handle = request.form['twitter_handle']
            facebook_handle = request.form['facebook_handle']
            youtube_handle = request.form['youtube_handle']

            # Additional form data for the course schedule
            start_date = request.form['start_date']
            end_date = request.form['end_date']
            days_of_week = request.form['days_of_week']
            class_time = request.form['class_time']

            try:
                db = firestore.client()
                doc_ref = db.collection('courses').document()

                course_data = {
                    'course_name': course_name,
                    'flyer_url': flyer_url,
                    'background_image_url': background_image_url,
                    'detailed_description': detailed_description,
                    'short_description': short_description,
                    'key_highlights': key_highlights,
                    'duration': duration,
                    'pre_requisite': pre_requisite,
                    'amount': float(amount),
                    'instructors_image_url': instructors_image_url,
                    'instructors_name': instructors_name,
                    'bio': bio,
                    'linkedin_handle': linkedin_handle,
                    'instagram_handle': instagram_handle,
                    'twitter_handle': twitter_handle,
                    'facebook_handle': facebook_handle,
                    'youtube_handle': youtube_handle,
                    'start_date': start_date,
                    'end_date': end_date,
                    'days_of_week': days_of_week,
                    'class_time': class_time
                }

                doc_ref.set(course_data)

                return "Course data uploaded successfully to Firebase."
            except Exception as e:
                return f"Error: {e}"

        elif 'event_flyer' in request.files:
            # Process event data upload
            event_flyer = request.files['event_flyer']
            event_flyer_url = upload_image_to_storage(event_flyer)

            # Get other form data for events
            event_name = request.form['event_name']
            event_background_image = request.files['event_background_image']
            event_background_image_url = upload_image_to_storage(event_background_image)
            event_detailed_description = request.form['event_detailed_description']
            event_short_description = request.form['event_short_description']
            event_date = request.form['event_date']
            event_time = request.form['event_time']
            event_location = request.form['event_location']
            event_amount = request.form['event_amount']

            # Rest of the host details
            host_image = background_image = request.files['host-image']
            host_image_url = upload_image_to_storage(host_image)
            host_name = request.form['host_name']
            host_bio = request.form['host_bio']
            host_linkedin_handle = request.form['host_linkedin_handle']
            host_instagram_handle = request.form['host_instagram_handle']
            host_twitter_handle = request.form['host_twitter_handle']
            host_facebook_handle = request.form['host_facebook_handle']
            host_youtube_handle = request.form['host_youtube_handle']

            try:
                db = firestore.client()
                doc_ref = db.collection('events').document()

                event_data = {
                    'event_name': event_name,
                    'event_flyer_url': event_flyer_url,
                    'event_background_image_url': event_background_image_url,
                    'event_detailed_description': event_detailed_description,
                    'event_short_description': event_short_description,
                    'event_date': event_date,
                    'event_time': event_time,
                    'event_location': event_location,
                    'event_amount': float(event_amount),
                    'host_image_url': host_image_url,
                    'host_name': host_name,
                    'host_bio': host_bio,
                    'host_linkedin_handle': host_linkedin_handle,
                    'host_instagram_handle': host_instagram_handle,
                    'host_twitter_handle': host_twitter_handle,
                    'host_facebook_handle': host_facebook_handle,
                    'host_youtube_handle': host_youtube_handle
                }

                doc_ref.set(event_data)

                return "Event data uploaded successfully to Firebase."
            except Exception as e:
                return f"Error: {e}"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

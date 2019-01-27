const functions = require('firebase-functions');
const admin = require("firebase-admin");
const serviceAccount = require("./barhelper-firebase-adminsdk-tyh7r-5a2f0eea5f.json");
require('path');

admin.initializeApp({
    credential: admin.credential.cert(serviceAccount),
    databaseURL: "https://barhelper.firebaseio.com"
});


// Create and Deploy Your First Cloud Functions
// https://firebase.google.com/docs/functions/write-firebase-functions

exports.imageUploaded = functions.storage.object().onFinalize(async object => {
    const fileBucket = object.bucket; // The Storage bucket that contains the file.
    const filePath = object.name; // File path in the bucket.
    const contentType = object.contentType; // File content type.
    const metageneration = object.metageneration; // Number of times metadata has been generated. New objects have a value of 1.

    const bucket = admin.storage().bucket(fileBucket);

    const url = await bucket.file(filePath).getSignedUrl();

    console.log(url);

    return url;

    // if (contentType.startsWith('image/')) {


    //     console.log("https://storage.googleapis.com/barhelper.appspot.com/bottle.jfif")

    //     console.log(signedUrls);

    //     return signedUrls;


    //     // console.log({
    //     //     fileBucket,
    //     //     filePath,
    //     //     contentType,
    //     //     metageneration
    //     // });
    // }
});
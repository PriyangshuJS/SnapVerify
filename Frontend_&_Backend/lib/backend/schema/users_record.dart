import 'dart:async';

import 'package:collection/collection.dart';

import '/backend/schema/util/firestore_util.dart';
import '/backend/schema/util/schema_util.dart';

import 'index.dart';
import '/flutter_flow/flutter_flow_util.dart';

class UsersRecord extends FirestoreRecord {
  UsersRecord._(
    DocumentReference reference,
    Map<String, dynamic> data,
  ) : super(reference, data) {
    _initializeFields();
  }

  // "email" field.
  String? _email;
  String get email => _email ?? '';
  bool hasEmail() => _email != null;

  // "display_name" field.
  String? _displayName;
  String get displayName => _displayName ?? '';
  bool hasDisplayName() => _displayName != null;

  // "phone_number" field.
  String? _phoneNumber;
  String get phoneNumber => _phoneNumber ?? '';
  bool hasPhoneNumber() => _phoneNumber != null;

  // "bio" field.
  String? _bio;
  String get bio => _bio ?? '';
  bool hasBio() => _bio != null;

  // "uid" field.
  String? _uid;
  String get uid => _uid ?? '';
  bool hasUid() => _uid != null;

  // "created_time" field.
  DateTime? _createdTime;
  DateTime? get createdTime => _createdTime;
  bool hasCreatedTime() => _createdTime != null;

  // "password" field.
  String? _password;
  String get password => _password ?? '';
  bool hasPassword() => _password != null;

  // "registration_photo" field.
  String? _registrationPhoto;
  String get registrationPhoto => _registrationPhoto ?? '';
  bool hasRegistrationPhoto() => _registrationPhoto != null;

  // "login_photo" field.
  String? _loginPhoto;
  String get loginPhoto => _loginPhoto ?? '';
  bool hasLoginPhoto() => _loginPhoto != null;

  // "photo_url" field.
  String? _photoUrl;
  String get photoUrl => _photoUrl ?? '';
  bool hasPhotoUrl() => _photoUrl != null;

  // "login_request" field.
  bool? _loginRequest;
  bool get loginRequest => _loginRequest ?? false;
  bool hasLoginRequest() => _loginRequest != null;

  void _initializeFields() {
    _email = snapshotData['email'] as String?;
    _displayName = snapshotData['display_name'] as String?;
    _phoneNumber = snapshotData['phone_number'] as String?;
    _bio = snapshotData['bio'] as String?;
    _uid = snapshotData['uid'] as String?;
    _createdTime = snapshotData['created_time'] as DateTime?;
    _password = snapshotData['password'] as String?;
    _registrationPhoto = snapshotData['registration_photo'] as String?;
    _loginPhoto = snapshotData['login_photo'] as String?;
    _photoUrl = snapshotData['photo_url'] as String?;
    _loginRequest = snapshotData['login_request'] as bool?;
  }

  static CollectionReference get collection =>
      FirebaseFirestore.instance.collection('users');

  static Stream<UsersRecord> getDocument(DocumentReference ref) =>
      ref.snapshots().map((s) => UsersRecord.fromSnapshot(s));

  static Future<UsersRecord> getDocumentOnce(DocumentReference ref) =>
      ref.get().then((s) => UsersRecord.fromSnapshot(s));

  static UsersRecord fromSnapshot(DocumentSnapshot snapshot) => UsersRecord._(
        snapshot.reference,
        mapFromFirestore(snapshot.data() as Map<String, dynamic>),
      );

  static UsersRecord getDocumentFromData(
    Map<String, dynamic> data,
    DocumentReference reference,
  ) =>
      UsersRecord._(reference, mapFromFirestore(data));

  @override
  String toString() =>
      'UsersRecord(reference: ${reference.path}, data: $snapshotData)';

  @override
  int get hashCode => reference.path.hashCode;

  @override
  bool operator ==(other) =>
      other is UsersRecord &&
      reference.path.hashCode == other.reference.path.hashCode;
}

Map<String, dynamic> createUsersRecordData({
  String? email,
  String? displayName,
  String? phoneNumber,
  String? bio,
  String? uid,
  DateTime? createdTime,
  String? password,
  String? registrationPhoto,
  String? loginPhoto,
  String? photoUrl,
  bool? loginRequest,
}) {
  final firestoreData = mapToFirestore(
    <String, dynamic>{
      'email': email,
      'display_name': displayName,
      'phone_number': phoneNumber,
      'bio': bio,
      'uid': uid,
      'created_time': createdTime,
      'password': password,
      'registration_photo': registrationPhoto,
      'login_photo': loginPhoto,
      'photo_url': photoUrl,
      'login_request': loginRequest,
    }.withoutNulls,
  );

  return firestoreData;
}

class UsersRecordDocumentEquality implements Equality<UsersRecord> {
  const UsersRecordDocumentEquality();

  @override
  bool equals(UsersRecord? e1, UsersRecord? e2) {
    return e1?.email == e2?.email &&
        e1?.displayName == e2?.displayName &&
        e1?.phoneNumber == e2?.phoneNumber &&
        e1?.bio == e2?.bio &&
        e1?.uid == e2?.uid &&
        e1?.createdTime == e2?.createdTime &&
        e1?.password == e2?.password &&
        e1?.registrationPhoto == e2?.registrationPhoto &&
        e1?.loginPhoto == e2?.loginPhoto &&
        e1?.photoUrl == e2?.photoUrl &&
        e1?.loginRequest == e2?.loginRequest;
  }

  @override
  int hash(UsersRecord? e) => const ListEquality().hash([
        e?.email,
        e?.displayName,
        e?.phoneNumber,
        e?.bio,
        e?.uid,
        e?.createdTime,
        e?.password,
        e?.registrationPhoto,
        e?.loginPhoto,
        e?.photoUrl,
        e?.loginRequest
      ]);

  @override
  bool isValidKey(Object? o) => o is UsersRecord;
}

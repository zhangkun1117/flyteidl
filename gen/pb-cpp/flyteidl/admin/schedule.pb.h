// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: flyteidl/admin/schedule.proto

#ifndef PROTOBUF_INCLUDED_flyteidl_2fadmin_2fschedule_2eproto
#define PROTOBUF_INCLUDED_flyteidl_2fadmin_2fschedule_2eproto

#include <limits>
#include <string>

#include <google/protobuf/port_def.inc>
#if PROTOBUF_VERSION < 3007000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers. Please update
#error your headers.
#endif
#if 3007000 < PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers. Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/port_undef.inc>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_table_driven.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/inlined_string_field.h>
#include <google/protobuf/metadata.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>  // IWYU pragma: export
#include <google/protobuf/extension_set.h>  // IWYU pragma: export
#include <google/protobuf/generated_enum_reflection.h>
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>
#define PROTOBUF_INTERNAL_EXPORT_flyteidl_2fadmin_2fschedule_2eproto

// Internal implementation detail -- do not use these members.
struct TableStruct_flyteidl_2fadmin_2fschedule_2eproto {
  static const ::google::protobuf::internal::ParseTableField entries[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::google::protobuf::internal::AuxillaryParseTableField aux[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::google::protobuf::internal::ParseTable schema[2]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::google::protobuf::internal::FieldMetadata field_metadata[];
  static const ::google::protobuf::internal::SerializationTable serialization_table[];
  static const ::google::protobuf::uint32 offsets[];
};
void AddDescriptors_flyteidl_2fadmin_2fschedule_2eproto();
namespace flyteidl {
namespace admin {
class FixedRate;
class FixedRateDefaultTypeInternal;
extern FixedRateDefaultTypeInternal _FixedRate_default_instance_;
class Schedule;
class ScheduleDefaultTypeInternal;
extern ScheduleDefaultTypeInternal _Schedule_default_instance_;
}  // namespace admin
}  // namespace flyteidl
namespace google {
namespace protobuf {
template<> ::flyteidl::admin::FixedRate* Arena::CreateMaybeMessage<::flyteidl::admin::FixedRate>(Arena*);
template<> ::flyteidl::admin::Schedule* Arena::CreateMaybeMessage<::flyteidl::admin::Schedule>(Arena*);
}  // namespace protobuf
}  // namespace google
namespace flyteidl {
namespace admin {

enum FixedRateUnit {
  MINUTE = 0,
  HOUR = 1,
  DAY = 2,
  FixedRateUnit_INT_MIN_SENTINEL_DO_NOT_USE_ = std::numeric_limits<::google::protobuf::int32>::min(),
  FixedRateUnit_INT_MAX_SENTINEL_DO_NOT_USE_ = std::numeric_limits<::google::protobuf::int32>::max()
};
bool FixedRateUnit_IsValid(int value);
const FixedRateUnit FixedRateUnit_MIN = MINUTE;
const FixedRateUnit FixedRateUnit_MAX = DAY;
const int FixedRateUnit_ARRAYSIZE = FixedRateUnit_MAX + 1;

const ::google::protobuf::EnumDescriptor* FixedRateUnit_descriptor();
inline const ::std::string& FixedRateUnit_Name(FixedRateUnit value) {
  return ::google::protobuf::internal::NameOfEnum(
    FixedRateUnit_descriptor(), value);
}
inline bool FixedRateUnit_Parse(
    const ::std::string& name, FixedRateUnit* value) {
  return ::google::protobuf::internal::ParseNamedEnum<FixedRateUnit>(
    FixedRateUnit_descriptor(), name, value);
}
// ===================================================================

class FixedRate final :
    public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:flyteidl.admin.FixedRate) */ {
 public:
  FixedRate();
  virtual ~FixedRate();

  FixedRate(const FixedRate& from);

  inline FixedRate& operator=(const FixedRate& from) {
    CopyFrom(from);
    return *this;
  }
  #if LANG_CXX11
  FixedRate(FixedRate&& from) noexcept
    : FixedRate() {
    *this = ::std::move(from);
  }

  inline FixedRate& operator=(FixedRate&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }
  #endif
  static const ::google::protobuf::Descriptor* descriptor() {
    return default_instance().GetDescriptor();
  }
  static const FixedRate& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const FixedRate* internal_default_instance() {
    return reinterpret_cast<const FixedRate*>(
               &_FixedRate_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    0;

  void Swap(FixedRate* other);
  friend void swap(FixedRate& a, FixedRate& b) {
    a.Swap(&b);
  }

  // implements Message ----------------------------------------------

  inline FixedRate* New() const final {
    return CreateMaybeMessage<FixedRate>(nullptr);
  }

  FixedRate* New(::google::protobuf::Arena* arena) const final {
    return CreateMaybeMessage<FixedRate>(arena);
  }
  void CopyFrom(const ::google::protobuf::Message& from) final;
  void MergeFrom(const ::google::protobuf::Message& from) final;
  void CopyFrom(const FixedRate& from);
  void MergeFrom(const FixedRate& from);
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  #if GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  static const char* _InternalParse(const char* begin, const char* end, void* object, ::google::protobuf::internal::ParseContext* ctx);
  ::google::protobuf::internal::ParseFunc _ParseFunc() const final { return _InternalParse; }
  #else
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input) final;
  #endif  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const final;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      ::google::protobuf::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(FixedRate* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return nullptr;
  }
  inline void* MaybeArenaPtr() const {
    return nullptr;
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const final;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // uint32 value = 1;
  void clear_value();
  static const int kValueFieldNumber = 1;
  ::google::protobuf::uint32 value() const;
  void set_value(::google::protobuf::uint32 value);

  // .flyteidl.admin.FixedRateUnit unit = 2;
  void clear_unit();
  static const int kUnitFieldNumber = 2;
  ::flyteidl::admin::FixedRateUnit unit() const;
  void set_unit(::flyteidl::admin::FixedRateUnit value);

  // @@protoc_insertion_point(class_scope:flyteidl.admin.FixedRate)
 private:
  class HasBitSetters;

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  ::google::protobuf::uint32 value_;
  int unit_;
  mutable ::google::protobuf::internal::CachedSize _cached_size_;
  friend struct ::TableStruct_flyteidl_2fadmin_2fschedule_2eproto;
};
// -------------------------------------------------------------------

class Schedule final :
    public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:flyteidl.admin.Schedule) */ {
 public:
  Schedule();
  virtual ~Schedule();

  Schedule(const Schedule& from);

  inline Schedule& operator=(const Schedule& from) {
    CopyFrom(from);
    return *this;
  }
  #if LANG_CXX11
  Schedule(Schedule&& from) noexcept
    : Schedule() {
    *this = ::std::move(from);
  }

  inline Schedule& operator=(Schedule&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }
  #endif
  static const ::google::protobuf::Descriptor* descriptor() {
    return default_instance().GetDescriptor();
  }
  static const Schedule& default_instance();

  enum ScheduleExpressionCase {
    kCronExpression = 1,
    kRate = 2,
    SCHEDULEEXPRESSION_NOT_SET = 0,
  };

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const Schedule* internal_default_instance() {
    return reinterpret_cast<const Schedule*>(
               &_Schedule_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    1;

  void Swap(Schedule* other);
  friend void swap(Schedule& a, Schedule& b) {
    a.Swap(&b);
  }

  // implements Message ----------------------------------------------

  inline Schedule* New() const final {
    return CreateMaybeMessage<Schedule>(nullptr);
  }

  Schedule* New(::google::protobuf::Arena* arena) const final {
    return CreateMaybeMessage<Schedule>(arena);
  }
  void CopyFrom(const ::google::protobuf::Message& from) final;
  void MergeFrom(const ::google::protobuf::Message& from) final;
  void CopyFrom(const Schedule& from);
  void MergeFrom(const Schedule& from);
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  #if GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  static const char* _InternalParse(const char* begin, const char* end, void* object, ::google::protobuf::internal::ParseContext* ctx);
  ::google::protobuf::internal::ParseFunc _ParseFunc() const final { return _InternalParse; }
  #else
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input) final;
  #endif  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const final;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      ::google::protobuf::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(Schedule* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return nullptr;
  }
  inline void* MaybeArenaPtr() const {
    return nullptr;
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const final;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // string kickoff_time_input_arg = 3;
  void clear_kickoff_time_input_arg();
  static const int kKickoffTimeInputArgFieldNumber = 3;
  const ::std::string& kickoff_time_input_arg() const;
  void set_kickoff_time_input_arg(const ::std::string& value);
  #if LANG_CXX11
  void set_kickoff_time_input_arg(::std::string&& value);
  #endif
  void set_kickoff_time_input_arg(const char* value);
  void set_kickoff_time_input_arg(const char* value, size_t size);
  ::std::string* mutable_kickoff_time_input_arg();
  ::std::string* release_kickoff_time_input_arg();
  void set_allocated_kickoff_time_input_arg(::std::string* kickoff_time_input_arg);

  // string cron_expression = 1;
  private:
  bool has_cron_expression() const;
  public:
  void clear_cron_expression();
  static const int kCronExpressionFieldNumber = 1;
  const ::std::string& cron_expression() const;
  void set_cron_expression(const ::std::string& value);
  #if LANG_CXX11
  void set_cron_expression(::std::string&& value);
  #endif
  void set_cron_expression(const char* value);
  void set_cron_expression(const char* value, size_t size);
  ::std::string* mutable_cron_expression();
  ::std::string* release_cron_expression();
  void set_allocated_cron_expression(::std::string* cron_expression);

  // .flyteidl.admin.FixedRate rate = 2;
  bool has_rate() const;
  void clear_rate();
  static const int kRateFieldNumber = 2;
  const ::flyteidl::admin::FixedRate& rate() const;
  ::flyteidl::admin::FixedRate* release_rate();
  ::flyteidl::admin::FixedRate* mutable_rate();
  void set_allocated_rate(::flyteidl::admin::FixedRate* rate);

  void clear_ScheduleExpression();
  ScheduleExpressionCase ScheduleExpression_case() const;
  // @@protoc_insertion_point(class_scope:flyteidl.admin.Schedule)
 private:
  class HasBitSetters;
  void set_has_cron_expression();
  void set_has_rate();

  inline bool has_ScheduleExpression() const;
  inline void clear_has_ScheduleExpression();

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  ::google::protobuf::internal::ArenaStringPtr kickoff_time_input_arg_;
  union ScheduleExpressionUnion {
    ScheduleExpressionUnion() {}
    ::google::protobuf::internal::ArenaStringPtr cron_expression_;
    ::flyteidl::admin::FixedRate* rate_;
  } ScheduleExpression_;
  mutable ::google::protobuf::internal::CachedSize _cached_size_;
  ::google::protobuf::uint32 _oneof_case_[1];

  friend struct ::TableStruct_flyteidl_2fadmin_2fschedule_2eproto;
};
// ===================================================================


// ===================================================================

#ifdef __GNUC__
  #pragma GCC diagnostic push
  #pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif  // __GNUC__
// FixedRate

// uint32 value = 1;
inline void FixedRate::clear_value() {
  value_ = 0u;
}
inline ::google::protobuf::uint32 FixedRate::value() const {
  // @@protoc_insertion_point(field_get:flyteidl.admin.FixedRate.value)
  return value_;
}
inline void FixedRate::set_value(::google::protobuf::uint32 value) {
  
  value_ = value;
  // @@protoc_insertion_point(field_set:flyteidl.admin.FixedRate.value)
}

// .flyteidl.admin.FixedRateUnit unit = 2;
inline void FixedRate::clear_unit() {
  unit_ = 0;
}
inline ::flyteidl::admin::FixedRateUnit FixedRate::unit() const {
  // @@protoc_insertion_point(field_get:flyteidl.admin.FixedRate.unit)
  return static_cast< ::flyteidl::admin::FixedRateUnit >(unit_);
}
inline void FixedRate::set_unit(::flyteidl::admin::FixedRateUnit value) {
  
  unit_ = value;
  // @@protoc_insertion_point(field_set:flyteidl.admin.FixedRate.unit)
}

// -------------------------------------------------------------------

// Schedule

// string cron_expression = 1;
inline bool Schedule::has_cron_expression() const {
  return ScheduleExpression_case() == kCronExpression;
}
inline void Schedule::set_has_cron_expression() {
  _oneof_case_[0] = kCronExpression;
}
inline void Schedule::clear_cron_expression() {
  if (has_cron_expression()) {
    ScheduleExpression_.cron_expression_.DestroyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
    clear_has_ScheduleExpression();
  }
}
inline const ::std::string& Schedule::cron_expression() const {
  // @@protoc_insertion_point(field_get:flyteidl.admin.Schedule.cron_expression)
  if (has_cron_expression()) {
    return ScheduleExpression_.cron_expression_.GetNoArena();
  }
  return *&::google::protobuf::internal::GetEmptyStringAlreadyInited();
}
inline void Schedule::set_cron_expression(const ::std::string& value) {
  // @@protoc_insertion_point(field_set:flyteidl.admin.Schedule.cron_expression)
  if (!has_cron_expression()) {
    clear_ScheduleExpression();
    set_has_cron_expression();
    ScheduleExpression_.cron_expression_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  }
  ScheduleExpression_.cron_expression_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:flyteidl.admin.Schedule.cron_expression)
}
#if LANG_CXX11
inline void Schedule::set_cron_expression(::std::string&& value) {
  // @@protoc_insertion_point(field_set:flyteidl.admin.Schedule.cron_expression)
  if (!has_cron_expression()) {
    clear_ScheduleExpression();
    set_has_cron_expression();
    ScheduleExpression_.cron_expression_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  }
  ScheduleExpression_.cron_expression_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::move(value));
  // @@protoc_insertion_point(field_set_rvalue:flyteidl.admin.Schedule.cron_expression)
}
#endif
inline void Schedule::set_cron_expression(const char* value) {
  GOOGLE_DCHECK(value != nullptr);
  if (!has_cron_expression()) {
    clear_ScheduleExpression();
    set_has_cron_expression();
    ScheduleExpression_.cron_expression_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  }
  ScheduleExpression_.cron_expression_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(),
      ::std::string(value));
  // @@protoc_insertion_point(field_set_char:flyteidl.admin.Schedule.cron_expression)
}
inline void Schedule::set_cron_expression(const char* value, size_t size) {
  if (!has_cron_expression()) {
    clear_ScheduleExpression();
    set_has_cron_expression();
    ScheduleExpression_.cron_expression_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  }
  ScheduleExpression_.cron_expression_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::string(
      reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:flyteidl.admin.Schedule.cron_expression)
}
inline ::std::string* Schedule::mutable_cron_expression() {
  if (!has_cron_expression()) {
    clear_ScheduleExpression();
    set_has_cron_expression();
    ScheduleExpression_.cron_expression_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  }
  // @@protoc_insertion_point(field_mutable:flyteidl.admin.Schedule.cron_expression)
  return ScheduleExpression_.cron_expression_.MutableNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline ::std::string* Schedule::release_cron_expression() {
  // @@protoc_insertion_point(field_release:flyteidl.admin.Schedule.cron_expression)
  if (has_cron_expression()) {
    clear_has_ScheduleExpression();
    return ScheduleExpression_.cron_expression_.ReleaseNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  } else {
    return nullptr;
  }
}
inline void Schedule::set_allocated_cron_expression(::std::string* cron_expression) {
  if (has_ScheduleExpression()) {
    clear_ScheduleExpression();
  }
  if (cron_expression != nullptr) {
    set_has_cron_expression();
    ScheduleExpression_.cron_expression_.UnsafeSetDefault(cron_expression);
  }
  // @@protoc_insertion_point(field_set_allocated:flyteidl.admin.Schedule.cron_expression)
}

// .flyteidl.admin.FixedRate rate = 2;
inline bool Schedule::has_rate() const {
  return ScheduleExpression_case() == kRate;
}
inline void Schedule::set_has_rate() {
  _oneof_case_[0] = kRate;
}
inline void Schedule::clear_rate() {
  if (has_rate()) {
    delete ScheduleExpression_.rate_;
    clear_has_ScheduleExpression();
  }
}
inline ::flyteidl::admin::FixedRate* Schedule::release_rate() {
  // @@protoc_insertion_point(field_release:flyteidl.admin.Schedule.rate)
  if (has_rate()) {
    clear_has_ScheduleExpression();
      ::flyteidl::admin::FixedRate* temp = ScheduleExpression_.rate_;
    ScheduleExpression_.rate_ = nullptr;
    return temp;
  } else {
    return nullptr;
  }
}
inline const ::flyteidl::admin::FixedRate& Schedule::rate() const {
  // @@protoc_insertion_point(field_get:flyteidl.admin.Schedule.rate)
  return has_rate()
      ? *ScheduleExpression_.rate_
      : *reinterpret_cast< ::flyteidl::admin::FixedRate*>(&::flyteidl::admin::_FixedRate_default_instance_);
}
inline ::flyteidl::admin::FixedRate* Schedule::mutable_rate() {
  if (!has_rate()) {
    clear_ScheduleExpression();
    set_has_rate();
    ScheduleExpression_.rate_ = CreateMaybeMessage< ::flyteidl::admin::FixedRate >(
        GetArenaNoVirtual());
  }
  // @@protoc_insertion_point(field_mutable:flyteidl.admin.Schedule.rate)
  return ScheduleExpression_.rate_;
}

// string kickoff_time_input_arg = 3;
inline void Schedule::clear_kickoff_time_input_arg() {
  kickoff_time_input_arg_.ClearToEmptyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline const ::std::string& Schedule::kickoff_time_input_arg() const {
  // @@protoc_insertion_point(field_get:flyteidl.admin.Schedule.kickoff_time_input_arg)
  return kickoff_time_input_arg_.GetNoArena();
}
inline void Schedule::set_kickoff_time_input_arg(const ::std::string& value) {
  
  kickoff_time_input_arg_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:flyteidl.admin.Schedule.kickoff_time_input_arg)
}
#if LANG_CXX11
inline void Schedule::set_kickoff_time_input_arg(::std::string&& value) {
  
  kickoff_time_input_arg_.SetNoArena(
    &::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::move(value));
  // @@protoc_insertion_point(field_set_rvalue:flyteidl.admin.Schedule.kickoff_time_input_arg)
}
#endif
inline void Schedule::set_kickoff_time_input_arg(const char* value) {
  GOOGLE_DCHECK(value != nullptr);
  
  kickoff_time_input_arg_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::string(value));
  // @@protoc_insertion_point(field_set_char:flyteidl.admin.Schedule.kickoff_time_input_arg)
}
inline void Schedule::set_kickoff_time_input_arg(const char* value, size_t size) {
  
  kickoff_time_input_arg_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(),
      ::std::string(reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:flyteidl.admin.Schedule.kickoff_time_input_arg)
}
inline ::std::string* Schedule::mutable_kickoff_time_input_arg() {
  
  // @@protoc_insertion_point(field_mutable:flyteidl.admin.Schedule.kickoff_time_input_arg)
  return kickoff_time_input_arg_.MutableNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline ::std::string* Schedule::release_kickoff_time_input_arg() {
  // @@protoc_insertion_point(field_release:flyteidl.admin.Schedule.kickoff_time_input_arg)
  
  return kickoff_time_input_arg_.ReleaseNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline void Schedule::set_allocated_kickoff_time_input_arg(::std::string* kickoff_time_input_arg) {
  if (kickoff_time_input_arg != nullptr) {
    
  } else {
    
  }
  kickoff_time_input_arg_.SetAllocatedNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), kickoff_time_input_arg);
  // @@protoc_insertion_point(field_set_allocated:flyteidl.admin.Schedule.kickoff_time_input_arg)
}

inline bool Schedule::has_ScheduleExpression() const {
  return ScheduleExpression_case() != SCHEDULEEXPRESSION_NOT_SET;
}
inline void Schedule::clear_has_ScheduleExpression() {
  _oneof_case_[0] = SCHEDULEEXPRESSION_NOT_SET;
}
inline Schedule::ScheduleExpressionCase Schedule::ScheduleExpression_case() const {
  return Schedule::ScheduleExpressionCase(_oneof_case_[0]);
}
#ifdef __GNUC__
  #pragma GCC diagnostic pop
#endif  // __GNUC__
// -------------------------------------------------------------------


// @@protoc_insertion_point(namespace_scope)

}  // namespace admin
}  // namespace flyteidl

namespace google {
namespace protobuf {

template <> struct is_proto_enum< ::flyteidl::admin::FixedRateUnit> : ::std::true_type {};
template <>
inline const EnumDescriptor* GetEnumDescriptor< ::flyteidl::admin::FixedRateUnit>() {
  return ::flyteidl::admin::FixedRateUnit_descriptor();
}

}  // namespace protobuf
}  // namespace google

// @@protoc_insertion_point(global_scope)

#include <google/protobuf/port_undef.inc>
#endif  // PROTOBUF_INCLUDED_flyteidl_2fadmin_2fschedule_2eproto
